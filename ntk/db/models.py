# Import gv object from ntk.objects
# gv is a global var object which
# can be used to set and get variables

from ntk.objects import gv as gv

# Import connect and disconnect from ntk.db.conn
# these are used to connect disconnect database efficiently

from ntk.db.conn import connect, disconnect

# import more libraries and modules
# that's are used to manipulate os level implementation

import json, os, datetime, string, random, time


# gdefault is get default


def gdefault(val):

    # gdefault function is used to parse a sql string which
    # can be attach with sql main query as a default supporter

    # it takes a parameter and assign it with
    # sql query string

    # check if value is passed properly

    if not val:

        # if not value is passed return an empty string

        return ""

    return " DEFAULT '{}'".format(val)


# gnull is get null


def gnull(val):

    # gnull function is used to parse a sql string which
    # can be attach with sql main query as a null supporter or not

    # it takes a parameter and assign it with
    # sql query string

    # check if value is passed properly

    if val:

        # if value is passed return an empty string

        return ""

    return " NOT NULL"


# etic_dict is exact_table_info create and get and set all table info from database


def etic_dict(cr=False):

    # etic_dict function is used to parse a sql string which
    # can be attach with sql main query as a null supporter or not

    # it takes a parameter and assign it with
    # sql query string

    # check if value is passed properly

    # crr = cr
    # if not crr:

    # get db and cursor object by connecting to database
    # see db.conn.connect to more info about connect function

    db, cr = connect()

    # let's create exact_table_info if it not created before

    cr.execute("CREATE TABLE IF NOT EXISTS exact_table_info (id INTEGER PRIMARY KEY, table_name TEXT, info BLOB)")

    # next get all table info from exact_table_info

    q = cr.execute("SELECT info FROM exact_table_info").fetchall()

    # next set default global var models as empty dictionary

    gv.models = {}

    # let's have a loop into all table info

    for sq in q:

        # in single info we now adding table columns info
        # by table name keyword

        for k,v in json.loads(sq['info']).items():

            # assign every column info in models by table name

            gv.models[k] = v

    # if not crr:

    # at last disconnect again the database

    disconnect(db)

# validate is for validating column value when inserting or updating


def validate(col, key, val):

    # validate function is used to validate column value passed
    # to insert or update query

    # check major type of validation by
    # their column type, raise error if anything is unwanted
    # else return main value

    # check column type is a email

    if col['type']=="email":

        # if column type is a email
        # we need to parse email validation

        try:

            # split left and right text from email by @

            beg, end = val.split('@')

            # check if every side is populated

            if len(beg)<1 or len(beg)>64 or len(end)<1 or len(end)>255:

                # if any side is empty or out of length
                # raise a value error containing the email

                raise ValueError("{} -> Email length is not in proper format".format(key))

        except Exception as e:
            gv.error_log(str(e))

            # check if null passable, then

            if col['null']:

                # return null because email not validated

                return None

        # if this portion executed, so that
        # email is valid with our validation, return the value

        return val

    elif col['type']=='boolean':

        # if column type is boolean, then
        # we need to check and validate this value
        # as a boolean value

        try:

            # check if value is zero or one

            if str(val) not in ['0', '1']:

                # if value is not in zero or one, then
                # we need to raise a value error containing this value

                raise ValueError("{} -> Boolean validation error".format(key))

        except Exception as e:
            gv.error_log(str(e))

            # check if column is nullable

            if col['null']:

                # if column is nullable, then
                # return the null value

                return None

        # if this portion is executed, so
        # our field values is validated properly
        # so we can return it

        return val

    elif col['type']=='datetime':

        # if column type is datetime, then
        # we need to check and validate this value
        # as a datetime value

        try:

            try:

                # try to get datetime value is in
                # column defined datetime format

                datetime.datetime.strptime(val, col['format'])

            except Exception as e:
                gv.error_log(str(e))

                # if datetime is not parsable to defined format
                # raise a value error, because it is not able to parse

                raise ValueError("{} -> DateTime format does not matching".format(key))

        except Exception as e:
            gv.error_log(str(e))

            # check if column is null supported,

            if col['null']:

                # if column is null supported, then
                # return null instead of datetime value

                return None

        # if this portion is executed, then
        # datetime value is validated by the process

        return val

    elif col['type']=='date':

        # if column type is date, then
        # we need to check and validate this value
        # as a date value

        try:

            try:

                # try to get date value is in
                # column defined date format

                datetime.datetime.strptime(val, col['format'])

            except Exception as e:
                gv.error_log(str(e))

                # if date is not parsable to defined format
                # raise a value error, because it is not able to parse

                raise ValueError("{} -> Date format does not matching".format(key))

        except Exception as e:
            gv.error_log(str(e))

            # check if column is null supported,

            if col['null']:

                # if column is null supported, then
                # return null instead of date value

                return None

        # if this portion is executed, then
        # date value is validated by the process

        return val

    elif col['type']=='time':

        # if column type is time, then
        # we need to check and validate this value
        # as a time value

        try:

            try:

                # try to get time value is in
                # column defined time format

                datetime.datetime.strptime(val, col['format'])

            except Exception as e:
                gv.error_log(str(e))

                # if time is not parsable to defined format
                # raise a value error, because it is not able to parse

                raise ValueError("{} -> Time format does not matching".format(key))

        except Exception as e:
            gv.error_log(str(e))

            # check if column is null supported,

            if col['null']:

                # if column is null supported, then
                # return null instead of time value

                return None

        # if this portion is executed, then
        # time value is validated by the process

        return val


# validate_table is for validating full table when inserting or updating


def validate_table(table, kwargs, update=False):

    # validate_table function is used to validate full table info
    # to insert or update query

    # check major type of validation by
    # their column type, raise error if anything is unwanted
    # else return main value

    # at first loop over table info dictionary

    for k,v in gv.models[table].items():

        # check most possible conditions to have sure
        # as if we can set column value to it's default value

        if not v.get('null',0) and not kwargs.get(k,0) and v.get('default',0) and not update:

            # set column value as default value

            kwargs[k] = v['default']

        elif v['type'] in ['datetime', 'date', 'time']:

            # checked if column type is in datetime date or time
            # so we are sure this column value is related
            # to datetime object and widget

            if not kwargs.get(k, 0) and v['auto_now_add'] and not update:

                # checked if column value is not got, and
                # value attribute auto_now_add allowed when inserting
                # then we can set default timestamp value to it

                kwargs[k] = datetime.datetime.now().strftime(v['format'])

            elif not kwargs.get(k, 0) and v['auto_now'] and update:

                # checked if column value is not got, and
                # value attribute auto_now allowed when updating
                # then we can set default timestamp value to it

                kwargs[k] = datetime.datetime.now().strftime(v['format'])

        elif v['type'] == "slug":

            # checked if column type is slug
            # so we are sure this column value is related
            # to a id or slug

            if kwargs.get(k):

                # checked if column value is got
                # then we can replace all space by not space
                # so all chars will be attached to one word

                kwargs[k] = str(kwargs[k]).replace(' ','')

            else:

                if not v['null'] and not update:

                    # checked if column value is not got,
                    # null is allowed or
                    # not and is it a update call or not

                    # then we can generate a new slug id for it

                    kwargs[k] = "".join(random.choice(string.ascii_uppercase+string.digits) for i in range(v['length']))

    # if this portion is executed, then
    # we are sure our all keyword value is validated
    # or pre populated with default value

    # so we can pass full object by returning it

    return kwargs


# Retrieve is a class to maintain select related query from table


class Retrieve:

    # Retrieve class will be a instance, it's highly
    # bindable and callable instance for retrieving
    # value by dynamic query as a orm perspective

    def __init__(self, query, cr=False, *args, **kwargs):

        super(Retrieve, self).__init__(*args, **kwargs)

        # Retrieve class takes at most two parameters
        # query params is getting query string
        # cr parameter is getting cursor object

        # set default result variable, db variable and done variable

        self.res, db, done = {}, False, 0

        # check if cursor object is passed or not

        if not cr:

            # if cursor object is not passed
            # then we need to connect database

            db, cr = connect()

        # next we are looping to execute select query

        exist_limit = gv.try_limit

        while exist_limit > 0:
            # we are looping while our query is not executed properly

            try:

                exist_limit -= 1

                # execute select query and get
                # cursor query object from database

                res = cr.execute("SELECT " + query)

                # if query object is returned

                # let's assign all keyword to result variable
                # by fetching all result from query object

                self.res['all'] = res.fetchall()

                # let's assign one keyword to result variable
                # by fetching one result from query object

                self.res['one'] = res.fetchone()

                # if all and one result is got
                # our done variable is True now

                done = 1

            except Exception as e:

                gv.error_log(str(e))

                # if something is wrong with executing query
                # wait some time and retry again after some time

                time.sleep(1)

        if not done:
            self.res['all'] = []
            self.res['one'] = {}

        if db:

            # if new database is connected so
            # disconnect it because it's not global

            disconnect(db)

    def all(self):

        # all method is to pass all result from query object
        # we assigned all result to result object before
        # so now we need to pass it

        return self.res['all']

    def one(self):

        # one method is to pass one result from query object
        # we assigned one result to result object before
        # so now we need to pass it

        return self.res['one']

    def first(self):

        # first method is to pass first result from query object
        # we assigned all result to result object before
        # so now we need to pass first element of it

        return self.res['all'][0] if self.res['all'] else {}

    def last(self):

        # last method is to pass last result from query object
        # we assigned all result to result object before
        # so now we need to pass last element of it

        return self.res['all'][-1] if self.res['all'] else {}

# QuerySet is a class to maintain CRUD query


class QuerySet:

    # QuerySet class will be a instance, it's highly
    # bindable and callable instance for executing read write update delete
    # query for all table

    def __init__(self, table, *args, **kwargs):

        super(QuerySet, self).__init__(*args, **kwargs)

        # QuerySet class takes table parameter
        # table param is getting table name

        # set QuerySet object table attribute to passed table

        self.table = table

    def create(self, transaction=False, returning='id', **kwargs):

        # create method is used to manage insert query
        # is takes two parameters transaction and another
        # is kwargs dictionary as all column value

        # check if any column value is got

        return_value = None

        if kwargs:
            try:
                # if column value is got let's loop into all kwargs items

                for k, v in kwargs.items():
                    # validate all column value if
                    # any of column is getting unexpected data
                    # it will be raised

                    validate(gv.models[self.table][k], k, v)

                # after all validate full table data before inserting
                # we will get keyword arguments object if everything
                # is validated and set default

                kwargs = validate_table(self.table, kwargs)

                # next generate column list string from all column passed

                cls = ", ".join('%s' % k for k in kwargs.keys())

                # next generate value list string from all value passed

                vls = ", ".join("'%s'" % k for k in kwargs.values())

                # next execute insert query to insert new value with defined columns

                gv.cr[self.table].execute("INSERT INTO {} ({}) VALUES({}) RETURNING {}".format(
                                                            self.table,  # table name
                                                            cls,  # columns string
                                                            vls,  # values string
                                                            returning
                                                        )
                                                    )

                return_value = gv.cr[self.table].fetchone()

                # check if transaction is allowed

                if not transaction:
                    # if not transaction is allowed, let's execute commit to save it

                    gv.db[self.table].commit()

                # most important, clear cache of this table, because new record is inserted

                gv.cache[self.table] = {}

            except Exception as e:
                gv.error_log('Row not inserted due to ' + str(e) + 'for {}'.format(kwargs))

        return return_value

    def update(self, transaction=False, where=False, returning=False, **kwargs):

        # update method is used to manage update query
        # is takes three parameters transaction, where and another
        # is kwargs dictionary as all column value

        # check if any column value is got

        return_value = None

        if kwargs:

            try:

                # check if where checking column is passed

                if where:

                    # if where is passed, then generate as string
                    # to declare where query from keyword

                    where = "{} = '{}'".format(where, kwargs.pop(where))

                else:

                    # if not where is passed, then get first
                    # key value of keyword to make it
                    # where clause, and kwargs will be reset

                    # get first element and rest of keywords

                    (wh_k, wh_v), *kwargs = kwargs.items()

                    # declare where query from first element

                    where, kwargs = "{} = '{}'".format(wh_k, wh_v), dict(kwargs)

                # next loop into all keyword

                for k,v in kwargs.items():

                    # validate each of element by it's predefined types

                    validate(gv.models[self.table][k], k, v)

                # after that we need to validate whole table
                # to validate all types

                kwargs = validate_table(self.table, kwargs, update=True)

                # next define set values by combining all items in a string

                sets = ", ".join("{} = '{}'".format(k,v) for k,v in kwargs.items())

                # execute update query where we passing
                # where sets and where position values

                sql_statement = "UPDATE {} SET {} WHERE {}".format(self.table, sets, where)

                if returning:
                    sql_statement = sql_statement + " RETURNING {}".format(returning)

                gv.cr[self.table].execute(sql_statement)

                return_value = gv.cr[self.table].fetchone()

                # check if transaction is passed

                if not transaction:
                    if returning:
                        gv.cr[self.table].execute("COMMIT")

                    # if transaction is not passed, then
                    # commit whole database

                    gv.db[self.table].commit()

                # if row is updated, then
                # clear table cache data because table data changed

                gv.cache[self.table] = {}

            except Exception as e:
                gv.error_log('Row not updated due to ' + str(e) + 'for {}'.format(kwargs))

        return return_value

    def create_all(self, all):

        # create_all method is used to manage list of create query
        # is takes one parameter all

        # start transaction before inserting
        # it will reduce time complexity

        gv.cr[self.table].execute("BEGIN TRANSACTION")

        try:

            # loop over all rows

            for obj in all:

                # for every row we can call create method to handle it
                # we just passing transaction as True
                # because we are in a transaction

                self.create(transaction=True, **obj)

            # after every single item insert query is inserted,
            # we can commit database now

            gv.cr[self.table].execute("COMMIT")

            # reset cache of this table
            # when new data is inserted

            gv.cache[self.table] = {}

        except Exception as e:
            gv.error_log(str(e))

            # if any error got from inserting row
            # database need to be rollback

            # rollback will used to clear and delete temporary data
            # which is created in the transaction timeline

            gv.cr[self.table].execute("ROLLBACK")

        # for secure execution we will execute commit again

        gv.db[self.table].commit()

    def update_all(self, all, where=False):

        # update_all method is used to manage list of update query
        # is takes two parameters all and where

        # start transaction before inserting
        # it will reduce time complexity

        gv.cr[self.table].execute("BEGIN TRANSACTION")

        try:

            # loop over all row

            for obj in all:

                # run update method with single row

                self.update(transaction=True, where=where, **obj)

            # when all row is updated, we need to commit the transaction

            gv.cr[self.table].execute("COMMIT")

            # after commit we need to clear cache for this table

            gv.cache[self.table] = {}

        except Exception as e:
            gv.error_log(str(e))

            # if any row updating returning any error,
            # we will rollback whole transaction

            gv.cr[self.table].execute("ROLLBACK")

        # for secure execution we will execute commit again

        gv.db[self.table].commit()

    def delete(self, where=""):

        # delete method is used to
        # perform delete query for any table

        # only one parameter is needed and that is where
        # but this parameter need to be a sql string
        # this where string will be passed to
        # sql delete query where

        # execute delete query and pass table name, where query

        gv.cr[self.table].execute("DELETE FROM {} {}".format(
                                                        self.table, # table name
                                                        where # where query
                                                    )
                                                )

        # after deleting commit database to save permanently

        gv.db[self.table].commit()

        # as if our table is updated we need to clear cache of this table

        gv.cache[self.table] = {}

    def delete_all(self):

        # delete_all method is used to
        # perform delete query for all info from table

        # be careful to call this method
        # it will flash all data from table

        # execute sql query for deleting data from table

        gv.cr[self.table].execute("DELETE FROM {}".format(self.table))

        # after deleting data, we need to commit database
        # if we want to save changes

        gv.db[self.table].commit()

        # clear cache of this table

        gv.cache[self.table] = {}

    def all(self):

        # all method is a reference method for QuerySet all method
        # it simply pass necessary parameters to QuerySet class

        # and bind all method from QuerySet class

        return Retrieve("* FROM %s" %self.table, gv.cr[self.table]).all()

    def filter(self, q=False, sep="or", search="*", like=False, orderby='id', formula='ASC', **kwargs):

        # filter method is used to
        # perform filter query for any table

        # it takes more then six parameters,
        # q is a query string
        # sep is separator between different column and value 'and' or 'or'
        # search is sql string which can be * or many columns separated by comma ','
        # if like is False then query will be by equal else query will be by like %str%
        # orderby is need to ordering by any column
        # formula is an order by formula ASC or DESC
        # kwargs key value will be column name value pairs
        # which will be used to find related rows

        # define ct as cache table reference

        ct = gv.cache[self.table]

        # define cache keyword string formula

        ck = "{} {} {} {} {}".format(q, sep, search, like, kwargs)

        # check if cache is available for this keyword

        if ct.get(ck,0):

            # if cache is available for this keyword
            # then return this cache to master

            return ct[ck]

        else:

            # define order by query to attach

            orby = " ORDER BY {} {}".format(
                                        orderby, # order by column
                                        formula # order by formula
                                    )

            # check if q is defined

            if q:

                # if q is defined, we don't need to parse new query
                # we will try to execute this query

                # assign retr as Retrieve object with this query

                retr = Retrieve(q, gv.cr[self.table])

            elif kwargs:

                # if q is not defined, let's check kwargs is available
                # if keyword is available,
                # this ntket will parse a query for this keyword

                # set sstr sub query for joining to main query
                # make sure to checking like or equal search in database table

                sstr = "{} LIKE('{}')" if like else "{}='{}'"

                # set fts as another sub query which is
                # a set of key value joined
                # it's a generated sub query string to compare data

                fts = " {} ".format(sep).join(sstr.format(k,v) for k,v in kwargs.items())

                # at last start query by all query attached
                # by passing all arguments and keyword arguments we will be able to
                # get dynamic Retrieve object for this query

                # set retr as Retrieve object by dynamic parameter we have got

                retr = Retrieve("{} FROM {} WHERE {}{}".format(
                                                            search, # search criteria
                                                            self.table, # table name
                                                            fts, # compare query
                                                            orby # order by query
                                                        ), gv.cr[self.table] # cursor object
                                                    )

            else:

                # if q is not defined, keyword is not also defined
                # we will pass parameters to Retrieve class
                # to get desire data in desire formula from all rows

                # set retr as Retrieve object by dynamic parameter we have got

                retr = Retrieve("{} FROM {}{}".format(
                                                search, # search criteria
                                                self.table,  # table name
                                                orby # order by
                                            ), gv.cr[self.table] # cursor object
                                        )

        # if new retr is got, let's add this result
        # in cache table

        ct[ck] = retr

        # after everything let's return Retrieve object

        return retr


# Model is a class to maintain Table Modeling System


class Model:

    def __init__(self, name=False, *args, **kwargs):

        super(Model, self).__init__(*args, **kwargs)

        # class Model can be inherited, to
        # be able to make table db instance

        # example:
        # """
        #
        #     class Users(Model):
        #         self.slug('id')
        #         self.text('email')
        #         self.boolean('is_active', default='1')
        #         self.datetime('create_date', auto_now_add=True)
        #
        #
        #     to create this table in database we need to initialize it
        #     users = Users().initialize()
        #
        #
        #     data can be create by calling the
        #     users.qset.create(email="test@ntk.com")
        #
        #
        #     data can be updated by calling the
        #     sers.qset.update(where='email', email="test@ntk.com", is_active='0')
        #
        #
        #     data can be get by doing
        #     user = users.qset.filter(email='test@ntk.com').first()
        #
        #
        #     data can be deleted by doing
        #     users.qset.delete(email='test@ntk.com')
        #
        #
        #     table can flash by doing
        #
        #     users.qset.delete_all()
        #
        # """

        # set model attribute name as passed name

        self.name = name

        # set model attribute dsql as default sql for table
        # a default id column will be added on top of everything

        self.dsql = {
                    'id': {
                        'type': 'int',
                        'default': 0,
                        'null': 0
                    }
                }

        # set model attribute table name as
        # passed name or get by class name
        # who's inherited this base model class

        # check if self.name passed and set

        if not self.name:

            # if self.name is not passed or set
            # set self.name as class name who's inherited this base class model

            self.name = type(self).__name__

        # next set model attribute name table as model attribute name

        self.table = self.name

        # check if table name is available in cache object or not

        if not gv.cache.get(self.table):

            # if table name is not in cache
            # set default cache an empty dictionary for this table name

            gv.cache[self.table] = {}

        # set default sql as head of create table schema

        self.sql = "CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY"

        # set default qset attribute of this model as
        # a QuerySet object with the given table name

        self.qset  = QuerySet(self.table)

        # check if database and cursor object for
        # this model specific created previously or not

        if not gv.db.get(self.table, 0) and not gv.cr.get(self.table, 0):

            # if database and cursor object is not create previously
            # then create and assign new objects to global var

            gv.db[self.table], gv.cr[self.table] = connect()

        # check if this model table is in global var or not

        if self.table in gv.models:

            # if this model table is in global var
            # then initialize now dsql as global var models info for this table

            self.dsql = dict((k,v) for k,v in gv.models[self.table].items())

    def add_column(self, type_, name, default=False, null=False):

        # model add_column is used to alter table or add a new column in table

        # if we are adding new column in table
        # so we need to update global var and dsql as this value

        # it takes up to four parameters
        # type_ is column type
        # name is column name
        # default is column default is not passed
        # null is column null possible or not

        gv.models[self.table][name] = self.dsql[name] = {
                'type': type_, # column type
                'default': default, # column default value
                'null': null # not null or null supported
            }

        # let's execute to alter table structure
        # to add a new column in this table

        # we are using this table specific cursor to
        # execute alter command

        gv.cr[self.table].execute(
                "ALTER TABLE {} ADD COLUMN {} {}{}{}".format(
                    self.table, # table name
                    name, # column name
                    type_.upper(), # column type in upper case format
                    gdefault(default), # get default value as parsed from gdefault function
                    gnull(null) # get null value as parsed from gnull function
                )
            )

        # let's execute to update exact_table_info
        # table data for this table

        # we are using this table specific cursor to
        # execute update command

        gv.cr[self.table].execute(
                "UPDATE exact_table_info SET info = '{}' WHERE table_name = '{}'".format(
                    json.dumps({self.table: self.dsql}), # json dumped table info in info column
                    self.table # table name
                )
            )

        # after doing everything we can save database
        # by commit database again

        gv.db[self.table].commit()

    def add_field(self, type_, name, default=False, null=False):

        # model add_field is used to add a field in table

        # it takes up to four parameters
        # type_ is column type
        # name is column name
        # default is column default is not passed
        # null is column null possible or not

        # increase sql size for this table schema
        # it's a dynamic allocation of every fields call

        self.sql = self.sql + ", {} {}{}{}".format(
                name, # column name
                type_.upper(), # type in upper case
                default, # default value for this column
                null # null or not null value for this column
            )

    def text(self, name, default=False, null=False):

        # model text is reference as model field type

        # it takes up to three parameters
        # name is column name
        # default is column default is not passed
        # null is column null possible or not

        # we need to update dsql at first
        # because after creating this table
        # every query will be parse by dsql parameters

        self.dsql[name] = {
                'type': 'text', # type as text
                'default': default, # default value
                'null': null # null or not null
            }

        # after doing that, we will add
        # this field actually in our sql,
        # for this we need to call add_field
        # method by passing important parameters

        self.add_field(
                "text", # type as text
                name, # name or column which is passed
                gdefault(default), # default query
                gnull(null) # null query
            )

    def slug(self, name, default=False, null=False, length=20):

        # model slug is reference as model field type

        # it takes up to four parameters
        # name is column name
        # default is column default is not passed
        # null is column null possible or not
        # length is slug word chars length

        # we need to update dsql at first
        # because after creating this table
        # every query will be parse by dsql parameters

        self.dsql[name] = {
                'type': 'slug', # type as slug
                'default': default, # default query
                'null': null, # null query
                'length': length # length integer
            }

        # after doing that, we will add
        # this field actually in our sql,
        # for this we need to call add_field
        # method by passing important parameters

        self.add_field(
                "text", # type as text
                name, # name which is passed
                gdefault(default), # default query
                gnull(null) # null query
            )

    def email(self, name, default=False, null=False, only=False, exclude=False):

        # model email is reference as model field type

        # it takes up to five parameters
        # name is column name
        # default is column default is not passed
        # null is column null possible or not
        # only is a advance methodologies, which will be used in future version
        # exclude is a advance methodologies, which will be used in future version

        # we need to update dsql at first
        # because after creating this table
        # every query will be parse by dsql parameters

        self.dsql[name] = {
                'type': 'email', # type as email
                'default': default, # default query
                'null': null, # null query
                'only': only, # only value
                'exclude': exclude # exclude value
            }

        # after doing that, we will add
        # this field actually in our sql,
        # for this we need to call add_field
        # method by passing important parameters

        self.add_field(
                "text", # type as text
                name, # name which is passed
                gdefault(default), # default query
                gnull(null) # null query
            )

    def int(self, name, default=False, null=False):

        # model int is reference as model field type

        # it takes up to three parameters
        # name is column name
        # default is column default is not passed
        # null is column null possible or not

        # we need to update dsql at first
        # because after creating this table
        # every query will be parse by dsql parameters

        self.dsql[name] = {
                'type': 'int', # type as integer
                'default': default, # default query
                'null': null # null query
            }

        # after doing that, we will add
        # this field actually in our sql,
        # for this we need to call add_field
        # method by passing important parameters

        self.add_field(
                "int", # type as integer
                name, # name which is passed
                gdefault(default), # default query
                gnull(null) # null query
            )

    def float(self, name, default=False, null=False):

        # model float is reference as model field type

        # it takes up to three parameters
        # name is column name
        # default is column default is not passed
        # null is column null possible or not

        # we need to update dsql at first
        # because after creating this table
        # every query will be parse by dsql parameters

        self.dsql[name] = {
                'type': 'real', # type as real/float
                'default': default, # default query
                'null': null # null query
            }

        # after doing that, we will add
        # this field actually in our sql,
        # for this we need to call add_field
        # method by passing important parameters

        self.add_field(
                "real", # type as real/float
                name, # name which is passed
                gdefault(default), # default query
                gnull(null) # null query
            )

    def boolean(self, name, default=False, null=False):

        # model boolean is reference as model field type

        # it takes up to three parameters
        # name is column name
        # default is column default is not passed
        # null is column null possible or not

        # we need to update dsql at first
        # because after creating this table
        # every query will be parse by dsql parameters

        self.dsql[name] = {
                'type': 'boolean', # type as boolean
                'default': default, # default query
                'null': null # null query
            }

        # after doing that, we will add
        # this field actually in our sql,
        # for this we need to call add_field
        # method by passing important parameters

        self.add_field(
                "boolean", # type as boolean
                name, # name which is passed
                gdefault(default), # default query
                gnull(null) # null query
            )

    def datetime(self, name, default=False, null=False, auto_now_add=False, auto_now=False, format="%Y-%m-%d %H:%M:%S"):

        # model datetime is reference as model field type

        # it takes up to six parameters
        # name is column name
        # default is column default is not passed
        # null is column null possible or not
        # auto_now_add is a allowance to set default data when record is creating
        # auto_now is a allowance to set default data when record is updating
        # format is a datetime format to set allowed datetime formatting

        # we need to update dsql at first
        # because after creating this table
        # every query will be parse by dsql parameters

        self.dsql[name] = {
                'type': 'datetime', # type as datetime
                'default': default, # default query
                'null': null, # null query
                'auto_now_add': auto_now_add, # auto value add when creating record
                'auto_now': auto_now, # auto value add when updating record
                'format': format # datetime formatting
            }

        # after doing that, we will add
        # this field actually in our sql,
        # for this we need to call add_field
        # method by passing important parameters

        self.add_field(
                "datetime", # type as datetime
                name, # name which is passed
                gdefault(default), # default query
                gnull(null) # null query
            )

    def date(self, name, default=False, null=False, auto_now_add=False, auto_now=False, format="%Y-%m-%d"):

        # model date is reference as model field type

        # it takes up to six parameters
        # name is column name
        # default is column default is not passed
        # null is column null possible or not
        # auto_now_add is a allowance to set default data when record is creating
        # auto_now is a allowance to set default data when record is updating
        # format is a datetime format to set allowed datetime formatting

        # we need to update dsql at first
        # because after creating this table
        # every query will be parse by dsql parameters

        self.dsql[name] = {
                'type': 'date', # type as date
                'default': default, # default query
                'null': null, # null query
                'auto_now_add': auto_now_add, # auto value add when creating record
                'auto_now': auto_now, # auto value add when updating record
                'format': format # date formatting
            }

        # after doing that, we will add
        # this field actually in our sql,
        # for this we need to call add_field
        # method by passing important parameters

        self.add_field(
                "date", # type as date
                name, # name which is passed
                gdefault(default), # default query
                gnull(null) # null query
            )

    def time(self, name, default=False, null=False, auto_now_add=False, auto_now=False, format="%H:%M:%S"):

        # model time is reference as model field type

        # it takes up to six parameters
        # name is column name
        # default is column default is not passed
        # null is column null possible or not
        # auto_now_add is a allowance to set default data when record is creating
        # auto_now is a allowance to set default data when record is updating
        # format is a datetime format to set allowed datetime formatting

        # we need to update dsql at first
        # because after creating this table
        # every query will be parse by dsql parameters

        self.dsql[name] = {
                'type': 'time', # type as time
                'default': default, # default query
                'null': null, # null query
                'auto_now_add': auto_now_add, # auto value add when creating record
                'auto_now': auto_now, # auto value add when updating record
                'format': format # date formatting
            }

        # after doing that, we will add
        # this field actually in our sql,
        # for this we need to call add_field
        # method by passing important parameters

        self.add_field(
                "time", # type as time
                name, # name which is passed
                gdefault(default), # default query
                gnull(null) # null query
            )

    def foreign(self, key_id, reference_table, reference_id, ondelete="SET NULL", onupdate="SET NULL"):

        # model foreign is reference as model field type

        # it takes up to five parameters
        # key_id is column name which is going info foreign key query
        # reference_table is table which is referenced
        # reference_id is column name in table which is referenced
        # ondelete is passed to sql query, when referenced row will be deleted this formula will be executed
        # onupdate is passed to sql query, when referenced row will be updated this formula will be executed

        # we need to update dsql at first
        # because after creating this table
        # every query will be parse by dsql parameters

        self.dsql['foreign_%s'%key_id] = {
                'type': 'foreign', # type as foreign
                'key_id': key_id, # foreign key id
                'reference_table': reference_table, # foreign key referenced table
                'reference_id': reference_id, # foreign key referenced table back populate id
                'ondelete': ondelete, # on delete execution
                'onupdate': onupdate # on update execution
            }

        # after doing that, we will add
        # this field actually in our sql,
        # for this we need to call add_field
        # method by passing important parameters

        self.sql = self.sql + ", FOREIGN KEY({}) REFERENCES {}({}) ON DELETE {} ON UPDATE {}".format(
                                                                    key_id, # reference key id in this table
                                                                    reference_table, # reference table name
                                                                    reference_id, # key id in referenced table
                                                                    ondelete, # on delete execution
                                                                    onupdate # on update execution
                                                                )

    def execute(self, sql):

        # execute method simply execute a sql query
        # which is passed in this method as a parameter

        # cursor object used from this table
        # specific cursor getting from global var

        # execute passed sql in cursor

        gv.cr[self.table].execute(sql)

        # save newly modified database by
        # committing in database connection object

        gv.db[self.table].commit()

    def initialize(self):

        # initialize method is most important method for model

        # because it's a method to create and
        # set a table in database to future use

        # if len(gv.models.keys())<16:

        # set this table info data into database
        # by inserting table info in exact_table_info table

        # etic_dict function actually doing that

        etic_dict(gv.cr[self.table])

        # check if table name in global var models

        if not self.table in gv.models:

            # if table name is not in global var, then
            # pre populate sql query to execute in cursor object

            self.sql = self.sql.format(self.table) + ")"

            # pre populate dsql to add in exact_table_info

            self.dsql = {'%s'%self.table: self.dsql}

            # let's execute populated sql in model specific
            # cursor object, to reduce db connection and
            # to get better concurrency

            gv.cr[self.table].execute(self.sql)

            # after that execute insert command for
            # inserting this table info in exact_table_info

            gv.cr[self.table].execute("INSERT INTO exact_table_info (table_name, info) VALUES('{}', '{}')".format(
                                                                            self.table, # table name
                                                                            json.dumps(self.dsql) # table info object
                                                                        )
                                                                    )

            # to save database modification
            # we need to commit database

            gv.db[self.table].commit()

            # after inserting new info we can update global variable tables info

            etic_dict(gv.cr[self.table])

        else:

            # define q as selecting table info from
            # exact_table_info where table_name is this table

            q = gv.cr[self.table].execute("SELECT * FROM exact_table_info WHERE table_name = '%s'" %self.table
                                          ).fetchone()

            # reset dsql to retrieved table info

            self.dsql = json.loads(q['info'])

    def columns(self):

        # model columns method is used to
        # find all columns name from a table

        # their have a simple trick to find columns name list

        return [r['name'] for r in gv.cr[self.table].execute(
                                "SELECT DISTINCT name FROM PRAGMA_TABLE_INFO('{}')".format(self.table)
                            ).fetchall()]

    def reset_table(self):

        # model reset_table is used to flash and
        # clean all info and data from database
        # about this table and re initialize it

        # at first drop the table from database

        gv.cr[self.table].execute("DROP TABLE %s" %self.table)

        # next delete table info from exact_table_info table
        # so that we can re initialize it

        gv.cr[self.table].execute("DELETE FROM exact_table_info WHERE table_name = '%s'" %self.table)

        # commit database changes

        gv.db[self.table].commit()

        # get and set new database tables info from etic_dict function

        etic_dict(gv.cr[self.table])

        # at last we can re initialize database
        # by simply calling model.initialize method

        self.initialize()
