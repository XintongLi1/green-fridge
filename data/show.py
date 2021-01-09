from .queries import Queries as qr


class show_page:
    def __init__(self, sort_by=1, ascending=True, *queries):
        # sort_by - {0: 'id', 1: 'rating', 2: 'total_time_in_second', 3: # of ingredients}
        self.sort_by = sort_by
        self.ascending = ascending
        self.result = queries[0]

        self.id_ = {}
        for q in queries[1:]:
            self.id_ = self.id_.union(set(q.id.to_list()))


    def display(self):

        if self.sort_by == 0:

            pass

        elif self.sort_by == 1:
            self.result.rating.fillna(4.0, inplace=True)
            pass

        elif self.sort_by == 2:
            self.result.totalTimeInSeconds.fillna(4400, inplace=True)
            pass

        elif self.sort_by == 3:
            pass
