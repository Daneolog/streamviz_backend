from flask_restplus import Namespace, Resource, fields
from src import mysql

api = Namespace('streams', description='Stream related operations')
parser = api.parser()

# parser.add_argument('username', location='args', default='daneolog')
# parser.add_argument('password', location='args', default='password')
# parser.add_argument('email', location='args', default='daneolog@gmail.com')


def get_dict(cursor):
    columns = [col[0] for col in cursor.description]
    rows = []
    row = cursor.fetchone()
    while row is not None:
        row = [None if i is None else str(i) for i in row]
        rows.append(dict(zip(columns, row)))
        row = cursor.fetchone()
    return rows


@api.route('')
class Streams(Resource):

    @api.expect(parser)
    def get(self):
        try:
            conn = mysql.get_db().cursor()
            conn.execute("select * from stream")
        except:
            return 'something went wrong'

        return get_dict(conn)
