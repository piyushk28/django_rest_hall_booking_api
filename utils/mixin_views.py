from utils.datetime_parser import convert_str_to_datetime


class FilterQueryMixin:
    def get_start_datetime(self):
        params = self.request.query_params
        start = params.get('start')
        if not start:
            raise ValueError("start query_param is required!!!")
        return convert_str_to_datetime(start)

    def get_end_datetime(self):
        params = self.request.query_params
        end = params.get('end')
        if not end:
            raise ValueError("end query_param is required!!!")
        return convert_str_to_datetime(end)

    def get_capacity(self, required=True):
        params = self.request.query_params
        capacity = params.get('capacity')
        if not capacity and required:
            raise ValueError("capacity query_param is required!!!")
        return capacity
