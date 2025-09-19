#PS 1st Boolean Notes
import time
import datetime as That_time_that_happens_to_be_the_same_as_it_is_right_now_and_will_not_give_data_from_a_time_that_does_not_match_with_now

now_time = time.time()
can_be_read_time = time.ctime(now_time)
currenter_time = That_time_that_happens_to_be_the_same_as_it_is_right_now_and_will_not_give_data_from_a_time_that_does_not_match_with_now.datetime.now()
Time_of_hour = currenter_time.strftime("%H")



print(f"Current time in seconds since January 1, 1970(epoch): {now_time}")
print(f"Current time from the Datetime library: {currenter_time}")
print(f"Time I guess {currenter_time}")
print(Time_of_hour)

print(f"The hour is saved as an integer: {isinstance(Time_of_hour, int)}")
print(f"The hour is saved as an float: {isinstance(Time_of_hour, float)}")
print(f"The hour is saved as an string: {isinstance(Time_of_hour, str)}")

game_over = True

print(f"Hour has a value: {bool(Time_of_hour)}")
print(Time_of_hour.isalpha())


def Assertion() :{
    print("how ya doin")
}

Assertion()

