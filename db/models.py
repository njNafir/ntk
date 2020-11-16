from ntk.objects import gv as gv
from ntk.db.conn import connect, disconnect
import json, os, datetime, string, random, time

def gdefault(val):
    return " DEFAULT '{}'".format(val) if val else ""

def gnull(val):
    return "" if val else " NOT NULL"

def etic_dict(cr=False):
    # crr = cr
    # if not crr:
    db, cr = connect()

    cr.execute("CREATE TABLE IF NOT EXISTS exact_table_info (id INTEGER PRIMARY KEY, table_name TEXT, info BLOB)")
    q = cr.execute("SELECT info FROM exact_table_info").fetchall()
    gv.models = {}
    for sq in q:
        for k,v in json.loads(sq['info']).items():
            gv.models[k] = v

    # if not crr:
    disconnect(db)

def validate(col, key, val):
    if col['type']=="email":
        try:
            beg, end = val.split('@')

            if len(beg)<1 or len(beg)>64 or len(end)<1 or len(end)>255:
                raise ValueError("{} -> Email length is not in proper format".format(key))

        except Exception as e:
            if col['null']:
                return None

        return val

    elif col['type']=='boolean':
        try:
            if str(val) not in ['0', '1']:
                raise ValueError("{} -> Boolean validation error".format(key))
        except Exception as e:
            if col['null']:
                return None

        return val

    elif col['type']=='datetime':
        try:
            try:
                datetime.datetime.strptime(val, col['format'])
            except Exception as e:
                raise ValueError("{} -> DateTime format does not matching".format(key))
        except Exception as e:
            if col['null']:
                return None

        return val

    elif col['type']=='date':
        try:
            try:
                datetime.datetime.strptime(val, col['format'])
            except Exception as e:
                raise ValueError("{} -> Date format does not matching".format(key))
        except Exception as e:
            if col['null']:
                return None

        return val

    elif col['type']=='time':
        try:
            try:
                datetime.datetime.strptime(val, col['format'])
            except Exception as e:
                raise ValueError("{} -> Time format does not matching".format(key))
        except Exception as e:
            if col['null']:
                return None

        return val

def validate_table(table, kwargs, update=False):
    for k,v in gv.models[table].items():
        if not v.get('null',0) and not kwargs.get(k,0) and v.get('default',0) and not update:
            kwargs[k] = v['default']
        elif v['type'] in ['datetime', 'date', 'time']:
            if not kwargs.get(k, 0) and v['auto_now_add'] and not update:
                kwargs[k] = datetime.datetime.now().strftime(v['format'])
            elif not kwargs.get(k, 0) and v['auto_now'] and update:
                kwargs[k] = datetime.datetime.now().strftime(v['format'])
        elif v['type'] == "slug":
            if kwargs.get(k):
                kwargs[k] = str(kwargs[k]).replace(' ','')
            else:
                if not v['null'] and not update:
                    kwargs[k] = "".join(random.choice(string.ascii_uppercase+string.digits) for i in range(v['length']))
    return kwargs

class Retrieve:
    def __init__(self, query, cr=False, *args, **kwargs):
        super(Retrieve, self).__init__(*args, **kwargs)
        self.res, db, done = {}, False, 0

        if not cr: db, cr   = connect()

        while done==0:
            try:
                res = cr.execute("SELECT " + query)
                self.res['all'] = res.fetchall()
                self.res['one'] = res.fetchone()
                done = 1
            except Exception as e:
                time.sleep(1)

        if db: disconnect(db)

    def all(self):
        return self.res['all']

    def one(self):
        return self.res['one']

    def first(self):
        return self.res['all'][0] if self.res['all'] else []

    def last(self):
        return self.res['all'][-1] if self.res['all'] else []

class QuerySet:
    def __init__(self, table, *args, **kwargs):
        super(QuerySet, self).__init__(*args, **kwargs)
        self.table = table

    def create(self, transaction=False, **kwargs):
        if kwargs:
            for k,v in kwargs.items():
                validate(gv.models[self.table][k], k, v)

            kwargs = validate_table(self.table, kwargs)

            cls = ", ".join('%s'%k for k in kwargs.keys())
            vls = ", ".join("'%s'"%k for k in kwargs.values())
            gv.cr[self.table].execute("INSERT INTO {} ({}) VALUES({})".format(self.table, cls, vls))
            if not transaction: gv.db[self.table].commit()

            gv.cache[self.table] = {}

    def update(self, transaction=False, where=False, **kwargs):
        if kwargs:
            if where:
                where = "{} = '{}'".format(where, kwargs.pop(where))
            else:
                (wh_k, wh_v), *kwargs = kwargs.items()
                where, kwargs = "{} = '{}'".format(wh_k, wh_v), dict(kwargs)

            for k,v in kwargs.items():
                validate(gv.models[self.table][k], k, v)

            kwargs = validate_table(self.table, kwargs, update=True)

            sets = ", ".join("{} = '{}'".format(k,v) for k,v in kwargs.items())

            gv.cr[self.table].execute("UPDATE {} SET {} WHERE {}".format(self.table, sets, where))
            if not transaction: gv.db[self.table].commit()

            gv.cache[self.table] = {}

    def create_all(self, all):
        gv.cr[self.table].execute("BEGIN TRANSACTION")

        try:
            for obj in all:
                self.create(transaction=True, **obj)

            gv.cr[self.table].execute("COMMIT")

            gv.cache[self.table] = {}
        except Exception as e:
            gv.cr[self.table].execute("ROLLBACK")

        gv.db[self.table].commit()

    def update_all(self, all, where=False):
        gv.cr[self.table].execute("BEGIN TRANSACTION")

        try:
            for obj in all:
                self.update(transaction=True, where=where, **obj)

            gv.cr[self.table].execute("COMMIT")

            gv.cache[self.table] = {}
        except Exception as e:
            gv.cr[self.table].execute("ROLLBACK")

        gv.db[self.table].commit()

    def delete(self, where=""):
        gv.cr[self.table].execute("DELETE FROM {} {}".format(self.table, where))
        gv.db[self.table].commit()

        gv.cache[self.table] = {}

    def delete_all(self):
        gv.cr[self.table].execute("DELETE FROM {}".format(self.table))
        gv.db[self.table].commit()

        gv.cache[self.table] = {}

    def all(self):
        return Retrieve("* FROM %s" %self.table, gv.cr[self.table]).all()

    def filter(self, q=False, sep="or", search="*", like=False, orderby='id', formula='ASC', **kwargs):
        ct = gv.cache[self.table]
        ck = "{} {} {} {} {}".format(q, sep, search, like, kwargs)

        if ct.get(ck,0):
            return ct[ck]
        else:
            orby = " ORDER BY {} {}".format(orderby, formula)

            if q:
                retr = Retrieve(q, gv.cr[self.table])
            elif kwargs:
                sstr = "{} LIKE('{}')" if like else "{}='{}'"
                fts = " {} ".format(sep).join(sstr.format(k,v) for k,v in kwargs.items())
                retr = Retrieve("{} FROM {} WHERE {}{}".format(search, self.table, fts, orby), gv.cr[self.table])
            else:
                retr = Retrieve("{} FROM {}{}".format(search, self.table, orby), gv.cr[self.table])

        ct[ck] = retr

        return retr

class Model:
    def __init__(self, name=False, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.name       = name
        self.dsql       = {'id': {'type': 'int', 'default': 0, 'null': 0}}
        self.table      = self.name if self.name else type(self).__name__
        if not gv.cache.get(self.table): gv.cache[self.table] = {}

        self.sql            = "CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY"
        self.qset           = QuerySet(self.table)

        if not gv.db.get(self.table, 0) and not gv.cr.get(self.table, 0):
            gv.db[self.table], gv.cr[self.table] = connect()

        if self.table in gv.models:
            self.dsql = dict((k,v) for k,v in gv.models[self.table].items())

    def add_column(self, type_, name, default=False, null=False):
        gv.models[self.table][name] = self.dsql[name] = {'type': type_, 'default': default, 'null': null}

        gv.cr[self.table].execute("ALTER TABLE {} ADD COLUMN {} {}{}{}".format(self.table, name, type_.upper(), gdefault(default), gnull(null)))
        gv.cr[self.table].execute("UPDATE exact_table_info SET info = '{}' WHERE table_name = '{}'".format(json.dumps({self.table: self.dsql}), self.table))
        gv.db[self.table].commit()

    def add_field(self, type_, name, default=False, null=False):
        self.sql = self.sql + ", {} {}{}{}".format(name, type_.upper(), default, null)

    def text(self, name, default=False, null=False):
        self.dsql[name] = {'type': 'text', 'default': default, 'null': null}
        self.add_field("text", name, gdefault(default), gnull(null))

    def slug(self, name, default=False, null=False, length=20):
        self.dsql[name] = {'type': 'slug', 'default': default, 'null': null, 'length': length}
        self.add_field("text", name, gdefault(default), gnull(null))

    def email(self, name, default=False, null=False, only=False, exclude=False):
        self.dsql[name] = {'type': 'email', 'default': default, 'null': null, 'only': only, 'exclude': exclude}
        self.add_field("text", name, gdefault(default), gnull(null))

    def int(self, name, default=False, null=False):
        self.dsql[name] = {'type': 'int', 'default': default, 'null': null}
        self.add_field("int", name, gdefault(default), gnull(null))

    def float(self, name, default=False, null=False):
        self.dsql[name] = {'type': 'real', 'default': default, 'null': null}
        self.add_field("real", name, gdefault(default), gnull(null))

    def boolean(self, name, default=False, null=False):
        self.dsql[name] = {'type': 'boolean', 'default': default, 'null': null}
        self.add_field("boolean", name, gdefault(default), gnull(null))

    def datetime(self, name, default=False, null=False, auto_now_add=False, auto_now=False, format="%Y-%m-%d %H:%M:%S"):
        self.dsql[name] = {'type': 'datetime', 'default': default, 'null': null, 'auto_now_add': auto_now_add, 'auto_now': auto_now, 'format': format}
        self.add_field("datetime", name, gdefault(default), gnull(null))

    def date(self, name, default=False, null=False, auto_now_add=False, auto_now=False, format="%Y-%m-%d"):
        self.dsql[name] = {'type': 'date', 'default': default, 'null': null, 'auto_now_add': auto_now_add, 'auto_now': auto_now, 'format': format}
        self.add_field("date", name, gdefault(default), gnull(null))

    def time(self, name, default=False, null=False, auto_now_add=False, auto_now=False, format="%H:%M:%S"):
        self.dsql[name] = {'type': 'time', 'default': default, 'null': null, 'auto_now_add': auto_now_add, 'auto_now': auto_now, 'format': format}
        self.add_field("time", name, gdefault(default), gnull(null))

    def foreign(self, key_id, reference_table, reference_id, ondelete="SET NULL", onupdate="SET NULL"):
        self.dsql['foreign_%s'%key_id] = {'type': 'foreign', 'key_id': key_id, 'reference_table': reference_table, 'reference_id': reference_id, 'ondelete': ondelete, 'onupdate': onupdate}
        self.sql = self.sql + ", FOREIGN KEY({}) REFERENCES {}({}) ON DELETE {} ON UPDATE {}".format(key_id, reference_table, reference_id, ondelete, onupdate)

    def execute(self, sql):
        gv.cr[self.table].execute(sql)
        gv.db[self.table].commit()

    def initialize(self):
        if len(gv.models.keys())<16:
            etic_dict(gv.cr[self.table])

        if not self.table in gv.models:
            self.sql = self.sql.format(self.table) + ")"
            self.dsql = {'%s'%self.table: self.dsql}

            gv.cr[self.table].execute(self.sql)
            gv.cr[self.table].execute("INSERT INTO exact_table_info (table_name, info) VALUES('{}', '{}')".format(self.table, json.dumps(self.dsql)))
            gv.db[self.table].commit()
            etic_dict(gv.cr[self.table])

        else:
            q = gv.cr[self.table].execute("SELECT * FROM exact_table_info WHERE table_name = '%s'" %self.table).fetchone()
            self.dsql = json.loads(q['info'])

    def columns(self):
        return [r['name'] for r in gv.cr[self.table].execute("SELECT DISTINCT name FROM PRAGMA_TABLE_INFO('{}')".format(self.table)).fetchall()]

    def reset_table(self):
        gv.cr[self.table].execute("DROP TABLE %s" %self.table)
        gv.cr[self.table].execute("DELETE FROM exact_table_info WHERE table_name = '%s'" %self.table)
        gv.db[self.table].commit()
        etic_dict(gv.cr[self.table])

        self.initialize()
