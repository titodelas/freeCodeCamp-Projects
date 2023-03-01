def add_time(start, duration, day=None):
    # Parse the start time
    start_time, meridian = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if meridian == 'PM':
        start_hour += 12

    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add the duration to the start time
    end_minute = (start_minute + duration_minute) % 60
    carry_hour = (start_minute + duration_minute) // 60
    end_hour = (start_hour + duration_hour + carry_hour) % 24
    carry_day = (start_hour + duration_hour + carry_hour) // 24

    # Format the end time
    if end_hour == 0:
        end_time = '12:%02d' % end_minute
        end_meridian = 'AM'
    elif end_hour < 12:
        end_time = '%d:%02d' % (end_hour, end_minute)
        end_meridian = 'AM'
    elif end_hour == 12:
        end_time = '12:%02d' % end_minute
        end_meridian = 'PM'
    else:
        end_time = '%d:%02d' % (end_hour - 12, end_minute)
        end_meridian = 'PM'

    # Add the day offset
    if day is not None:
        day = day.capitalize()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = days.index(day)
        end_day_index = (day_index + carry_day) % 7
        end_day = days[end_day_index]
        if carry_day == 1:
            end_time += ', ' + end_day + ' (next day)'
        elif carry_day > 1:
            end_time += ', ' + end_day + ' (%d days later)' % carry_day
        else:
            end_time += ', ' + end_day

    else:
        if carry_day == 1:
            end_time += ' (next day)'
        elif carry_day > 1:
            end_time += ' (%d days later)' % carry_day

    return end_time
