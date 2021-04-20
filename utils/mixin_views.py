class FilterQueryMixin:
    def get_start_datetime(self, required=True):
        params = self.request.query_params
        start = params.get('start')
        if not start and required:
            raise ValueError("start query_param is required!!!")
        return start

    def get_end_datetime(self, required=True):
        params = self.request.query_params
        end = params.get('end')
        if not end and required:
            raise ValueError("end query_param is required!!!")
        return end

    def get_capacity(self, required=True):
        params = self.request.query_params
        capacity = params.get('capacity')
        if not capacity and required:
            raise ValueError("capacity query_param is required!!!")
        return capacity
