# User Input
val = int(input('Enter any integer: '))
# Logic -- Hours Minutes Secs
x1 = (val / 60)
# Cal Secs
secs = (val % 60)
x2 = (x1 / 60)
# Cal minutes
minutes = (x1 % 60)
# Cal days
days = (x2 / 24)
# Cal hours
hours = (x2 % 24)

print str(days) + ' ' + 'days', \
      str(hours) + ' ' + 'hours', \
      str(minutes) + ' ' + 'minutes', \
      str(secs) + ' ' + 'secs'
