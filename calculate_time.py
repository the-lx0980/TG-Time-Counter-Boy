# Lx 0980
import calendar

def is_leap_year(year):
   return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def total_days_in_year(year):
    if is_leap_year(year):
        return 366  
    else:
        return 365  

def get_data(cur_year = 0,
            cur_month = 0,
            cur_day = 0,
            cur_hour = 0,
            cur_minute = 0):
     # Default         
    start_year = 2023    
    start_month = 9
    start_day = 3
    start_hour = 0
    start_minute = 0 

    # Set To 0
    total_years = 0
    total_months = 0
    total_days = 0
    total_hours = 0
    total_minutes = 0
              
    if cur_year - start_year > 2 or cur_year - start_year == 2:
        to_days, c_month = 0, 0
        for x in range(start_year, cur_year):
            total_days = total_days_in_year(x)
            to_days = to_days + total_days
            c_month += 12
        c_d = 0
        cu_t_d, c_month2, c_month1 = 0, 0, 0
        if cur_month > 1:
            for x in range(1, cur_month):# start_month):
               if 13 > x:
                 cu_d_m = calendar.monthrange(cur_year, x)[1]
                 cu_t_d = cu_d_m + cu_t_d
                 c_month1 += 1
        if start_month > 1:
            for x in range(1, start_month):# start_month):
               if 13 > x:
                 t_d_m = calendar.monthrange(start_year, x)[1]
                 c_d = c_d + t_d_m
                 c_month2 += 1
        total_days =  (cu_t_d + to_days + cur_day) - (c_d + start_day)
        total_months = (c_month + c_month1) - c_month2
        total_years = total_months/12
        total_hours = total_days * 24
        total_minutes = total_hours * 60
        print('Kaisa hai', total_days)
    elif cur_year == start_year and cur_month > start_month:
        total_days = total_days_in_year(cur_year)
        c_d  = 0
        for i in range(start_month, cur_month):
            if 13 > i:
              t_d_m = calendar.monthrange(cur_year, i)[1]
              c_d = c_d + t_d_m
        c_d = (c_d + cur_day) - start_day
        total_hours = ((c_d * 24) + cur_hour) - start_hour
        total_minutes = ((c_d * 24 * 60) + cur_minute) - start_minute
        total_days = c_d
        total_months = c_d/30
        if 30 > total_days:
            total_months = 0
        print('How are You')  
    elif start_year + 1 == cur_year:
        total_days, total_days2 = (total_days_in_year(start_year),
            total_days_in_year(cur_year))
        add_d, add_d1, Hours, Hours1, month, month1 = 0, 0, 0, 0, 0, 0
        for x in range(1, start_month):
            if 13 > x:
                c_m_d = calendar.monthrange(cur_year, x)[1]
                add_d += c_m_d
                Hours += 24 * add_d
                month += 1
        for x in range(1, cur_month):
            if 13 > x:
                c_m_d1 = calendar.monthrange(cur_year, x)[1]
                add_d1 += c_m_d1
                Hours1 += 24 * add_d1
                month1 += 1
        total_days = ((total_days - add_d) + add_d1 + cur_day) - start_day
        total_months = total_days/30 # (12 - start_month) + month1 if (12 - start_month) + month1 else  total_days/30
        if total_months > 12:
            total_years = 1
        total_hours = 24 * total_days
        total_minutes = total_hours * 60
        print('From 2023 - 2024')
    elif start_year == cur_year and start_month == cur_month:
        if cur_day > start_day:
            total_days = cur_day - start_day
            total_hours = (cur_hour + (24 * total_days) - start_hour)
            total_minutes = (cur_minute + (total_hours * 60) - start_minute)
            if 24 > total_hours:
                total_days = 0
            if 30 > total_days:
                total_months = 0
            else:
                total_months = total_days/30    
            print('Hello')
    if start_month == cur_month and start_year == cur_year and start_day == cur_day:
        if cur_hour > start_hour:
          total_hours = cur_hour - start_hour
          total_minutes = (((total_hours * 60) + cur_minute) - start_minute)
          if 60 > total_minutes: 
              total_hours = 0
          print('From Only Hours')
    if start_month == cur_month and start_year == cur_year and cur_day == start_day and cur_hour == start_hour:
           if cur_hour == start_hour:
               if start_minute < cur_minute:
                  total_minutes = cur_minute - start_minute
                  print('From Only Minutes')
    return total_years, total_months, total_days, total_hours, total_minutes            
