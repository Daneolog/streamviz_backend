from flask import send_from_directory, request
from flask_restplus import Namespace, Resource, fields
from src import db
from .clean import clean

api = Namespace('streams', description='Stream related operations')
parser = api.parser()

# parser.add_argument('username', location='args', default='daneolog')
# parser.add_argument('password', location='args', default='password')
# parser.add_argument('email', location='args', default='daneolog@gmail.com')


@api.route('')
class Streams(Resource):

    @api.expect(parser)
    def get(self):
        conn = db.get_engine()
        query = conn.execute("select * from stream")
        rows = []
        for row in query:
            row = dict(row)
            if row['date'] is not None:
                row['date'] = row['date'].strftime('%m/%d/%Y')
            rows.append(row)

        return rows


@api.route('/download')
class Download(Resource):

    @api.expect(parser)
    def get(self):
        return send_from_directory('../data', 'UOWN_data_master_04nov2018_clean.csv')


@api.route('/upload')
class Upload(Resource):

    @api.expect(parser)
    def post(self):
        csv = request.files['file']
        csv.save(f'new_data/{csv.filename}')

        df = clean(f'new_data/{csv.filename}')
        df.to_sql('stream', db.get_engine(), index=False, if_exists='append')
        return 'received'
