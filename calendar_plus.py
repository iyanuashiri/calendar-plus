from calendar import HTMLCalendar


class ModelCalendar(HTMLCalendar):

    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(ModelCalendar, self).__init__()

    def formatday(self, day, query):
        objects_per_day = query
        d = ''

        for object_ in objects_per_day:
            d += '<li>{0}</li>'.format(object_.get_html_url)

        if day != 0:
            return "<td><span>{0}</span><ul> {1} </ul></td>".format(day, d)
        return '<td></td>'

    def formatweek(self, theweek, query):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, query)
        return '<tr>{}</tr>'.format(week)

   