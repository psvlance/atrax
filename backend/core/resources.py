import logging
import json

from flask_restful import Resource
from flask import request, Response


log = logging.getLogger(__name__)


class MongoResource(Resource):
    @staticmethod
    def get_resource(name: str, handler: callable, database: callable):
        cls = type(
            f"MongoResource{name.capitalize()}",
            (MongoResource, ),
            {
                'handler': handler,
                'database': database,
            }
        )
        return cls

    def get(self, **kwargs):
        params = kwargs.copy()
        params.update(request.args)

        try:
            ans = self.handler(db=self.database, **params)
        except Exception as e:
            log.error(f'ERROR: {e}')
            ans = None

        if ans is not None:
            return Response({'answer': ans}, status=200, mimetype='application/json')
        else:
            return Response({'error': 'Request are wrong or database problem'}, status=500, mimetype='application/json')
