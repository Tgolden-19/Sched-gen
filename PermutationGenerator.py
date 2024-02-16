"""
Product of Tristan Golden
Date: 12/23/21
A tree object containing all the permutations of a possible weekly schedule with morning and night shifts (main shifts)
does not account for special cases like closers and pharma as they are extreme circumstances
"""
import random as rand
import numpy as np

class PermutationTree(object):
    debug = False
    permslist = ''
    startoff = None
    startam = None
    startpm = None
    treedepth = 0
    def __init__(self, depthlim):
        self.treedepth = depthlim
        self.startoff = PermutationNode(1, 0, depthlim, None)
        self.startam = PermutationNode(1, 1, depthlim, None)
        self.startpm = PermutationNode(1, 2, depthlim, None)
        self.permslist = self.cumulate_perms()

        if self.debug:
            print(self.startoff)
            print(self.startam)
            print(self.startpm)

    def cumulate_perms(self):
        perms = [0]*3
        offstart = self.startoff.forward_prop_recurs()
        amstart = self.startam.forward_prop_recurs()
        pmstart = self.startpm.forward_prop_recurs()

        if self.debug:
            print(offstart)
            print(amstart)
            print(pmstart)

        perms[0] = offstart
        if self.debug:
            print(perms)
        perms[1] = amstart
        if self.debug:
            print(perms)
        perms[2] = pmstart
        if self.debug:
            print(perms)
        return offstart + '\n' + amstart + '\n' + pmstart

    def set_perms(self, list):
        self.permslist = list

    def get_perms(self):
        return self.permslist

    def get_startoff(self):
        return self.startoff

    def set_startoff(self, newoff):
        self.startoff = newoff

    def get_startam(self):
        return self.startam

    def set_startam(self, newam):
        self.startam = newam

    def get_startpm(self):
        return self.startpm

    def set_startpm(self, newpm):
        self.startpm = newpm

    def get_depth(self):
        return self.treedepth

    def to_arr_by_week_num(self):
        return self.cumulate_perms().split('\n')

    def set_arr_by_week_num(self):
        self.set_perms(self.to_arr_by_week_num())


    def to_arr_day_num(self):
        temp = self.to_arr_by_week_num()
        for i in range(len(temp)):
            temp[i] = temp[i].split(",")
        return temp


    def to_num_arr_int(self):
        temp = self.to_arr_day_num()
        temp2 = [list(map(int, i)) for i in temp]
        return temp2


    def set_arr_day_num(self):
        self.set_perms(self.to_arr_day_num())

    def translate_str_list(self, section):
        section = section.replace("0", 'Off,')
        section = section.replace('1', 'AM,')
        section = section.replace('2', 'PM,')
        return section

    def translate_arr_list_self(self):
        """
        translates a 2d array of possible weeks of a schedule and returns it
        :param list: 2d array of schedule weeks in numbers
        :return: translated version of the 2d array
        """
        temp = self.cumulate_perms()
        for i in range(len(temp)):
            for j in range(len(i)):
                if temp[i][j] == 0:
                    temp[i][j] = "Off"
                elif temp[i][j] == 1:
                    temp[i][j] = "AM"
                else:
                    temp[i][j] = "PM"
        return temp

    def translate_arr_list(self, section):
        """
        translates a 2d array of possible weeks of a schedule and returns it
        :param list: 2d array of schedule weeks in numbers
        :return: translated version of the 2d array
        """
        temp = section
        for i in range(len(temp)):
            for j in range(len(i)):
                if temp[i][j] == 0:
                    temp[i][j] = "Off"
                elif temp[i][j] == 1:
                    temp[i][j] = "AM"
                else:
                    temp[i][j] = "PM"
        return temp

    def set_str_translate(self):
        self.set_perms(self.translate_str_list())

    def array_trans_week(self):
        temp = self.translate_str_list()
        temp = temp.split('\n')
        return temp

    # def set_array_trans_week(self, list):
    #     self.set_perms(self.array_trans_week(list))

    def array_trans_day(self):
        temp = self.array_trans_week()
        temp = temp.split(",")
        return temp

    # def set_arr_trans_day(self, list):
    #     self.set_perms(self.array_trans_day(list))

    def day_off_max_restrict(self, list):
        temp = list
        toremove = []
        for i in temp:
            countoff = 0
            # print(i)
            for j in i:
                if j == 0:
                    # print("another day off counted")
                    countoff += 1
                    # print(countoff)
                if countoff > 2:
                    # print("removing week template")
                    toremove.append(i)
                    break
        # print("number of weeks being removed by max day restrictor: " + str(len(toremove)))
        for i in toremove:
            temp.remove(i)

        # print("new number of templates after max day restrictor: " + str(len(temp)))
        return temp

    def day_off_max_restrict_self(self):
        temp = self.to_num_arr_int()
        # print(len(temp))
        temp = self.day_off_max_restrict(temp)
        # print(len(temp))
        return temp

    def day_off_min_restrict(self, list):
        temp = list
        toremove = []
        for i in temp:
            countoff = 0
            # print(i)
            for j in i:
                if j == 0:
                    # print("another day off counted")
                    countoff += 1
                    # print(countoff)

            if countoff < 2:
                # print("removing week template")
                toremove.append(i)
        # print("number of weeks being removed by minimum off day restrictor: " + str(len(toremove)))
        for i in toremove:
            temp.remove(i)

        # print("new number of templates after minimum off day restrictor: " + str(len(temp)))
        return temp

    def day_off_min_restrict_self(self):
        temp = self.to_num_arr_int()
        temp = self.day_off_min_restrict(temp)
        return temp

    def only_5_wrk_days(self, list):
        temp = self.day_off_max_restrict(list)
        temp = self.day_off_min_restrict(temp)
        return temp

    def only_5_wrk_days_self(self):
        temp = self.to_num_arr_int()
        temp = self.only_5_wrk_days(temp)
        return temp

    def no_clopens(self, section):
        temp = section
        toremove = []
        for i in temp:
            prevval = 0
            # print(i)
            for j in i:
                currval = j
                # print("currval = " + str(currval))
                # print("prevval = " + str(prevval))
                if currval == 1 and prevval == 2:
                    # print("found a clopen!")
                    toremove.append(i)
                    break
                prevval = j

        # print("number of weeks being removed by clopen eliminator: " + str(len(toremove)))
        for i in toremove:
            temp.remove(i)

        # print("new number of templates after clopen eliminator: " + str(len(temp)))

        return temp

    def no_clopens_self(self):
        temp = self.to_num_arr_int()
        temp = self.no_clopens(temp)
        return temp

    def full_restriction(self, section):
        temp = []
        temp = temp + section
        temp = self.only_5_wrk_days(temp)
        temp = self.no_clopens(temp)
        return temp

    def full_restriction_self(self):
        temp = self.to_num_arr_int()
        temp = self.full_restriction(temp)
        return temp

    def max_hours_restrict(self, section):
        temp = section
        temp = self.day_off_min_restrict(temp)
        temp = self.no_clopens(temp)
        return temp

    def max_hours_restrict_self(self):
        temp = self.to_num_arr_int()
        temp = self.max_hours_restrict(temp)
        return temp

    def week2_eliminator(self, option, firstday, lastday):

        temp = option.copy()
        temp = self.w2_elim_p1(temp, firstday)
        temp = self.w2_elim_p2(temp, lastday)
        temp = self.w2_elim_p3(temp, lastday)
        temp = self.w2_elim_p4(temp, firstday)

        return temp

    def w2_elim_p1(self, option, firstday):
        temp = option.copy()
        toremove = []
        if firstday == 0:
            for i in temp:
                if int(i[len(i)-1]) == 0:
                    toremove.append(i)

        if len(toremove) > 0:
            for j in toremove:
                temp.remove(j)
        return temp

    def w2_elim_p2(self, option, lastday):
        temp = option.copy()
        toremove = []
        if lastday == 0:
            for i in temp:
                if int(i[0]) == 0:
                    toremove.append(i)

        if len(toremove) > 0:
            for j in toremove:
                temp.remove(j)
        return temp

    def w2_elim_p3(self, option, lastday):
        temp = option.copy()
        toremove = []
        if lastday > 0:
            for i in temp:
                if int(i[0]) > 0:
                    toremove.append(i)

        if len(toremove) > 0:
            for j in toremove:
                temp.remove(j)
        return temp

    def w2_elim_p4(self, option, firstday):
        temp = option.copy()
        toremove = []
        if firstday > 0:
            for i in temp:
                if int(i[len(i)-1]) > 0:
                    toremove.append(i)

        if len(toremove) > 0:
            for j in toremove:
                temp.remove(j)
        return temp




# starting over from here

    def bridge_weeks(self, arr1, arr2):
        assert len(arr1) == len(arr2), "The 2 arrays are not of equal length. They may not have filled properly; recheck"
        mergedarr = []
        for i in range(len(arr1)):
            temp = arr1[i] + arr2[i]
            mergedarr.append(temp.copy())

        return mergedarr

    def check_conflicts(self, arr1, arr2):
        assert len(arr1) == len(
            arr2), "The 2 arrays are not of equal length. They may not have filled properly; recheck"

        for i in range(len(arr1)):
            if arr1[i][0] == 0 and arr2[i][len(arr2)-1] == 0:
                print("the arrays failed the conflict test")
                return True

            elif arr1[i][0] > 0 and arr2[i][len(arr2) - 1] > 0:
                print("the arrays failed the conflict test")
                return True

            elif arr1[i][len(arr1)-1] == 0 and arr2[i][0] == 0:
                print("the arrays failed the conflict test")
                return True

            elif arr1[i][len(arr1)-1] > 0 and arr2[i][0] > 0:
                print("the arrays failed the conflict test")
                return True

        print("The arrays passed the conflict test (Returning False because no conflicts found")
        return False

    def check_day_limits(self, arr, num_pos, day):

        countam = 0
        countpm = 0

        for j in arr:
            if j[day] == 2:
                countpm += 1

            if j[day] == 1:
                countam += 1

        # print(countam, countpm)
        if countam >= num_pos and countpm >= num_pos:
            # print("both am and pm limits have been reached for day: " + str(day))
            return True, True

        elif countam >= num_pos:
            # print("am limits have been reached for day: " + str(day))
            return True, False

        elif countpm >= num_pos:
            # print("pm limits have been reached for day: " + str(day))
            return False, True

        # print("Neither weekly limits have been reached for day: " + str(day))
        return False, False

    def check_week_limits(self, arr, num_pos):

        assert len(arr) > 1, "the length of the array is not 1 or more in size(not multiple weeks). Only use this function with multiple weeks in place already"
        weeklim = []

        for i in range(len(arr[0])):
            daylim = self.check_day_limits(arr, num_pos, i)
            weeklim.append(daylim)

        return weeklim

    def new_week_over_lim(self, multarrs, weekarr, num_pos):

        temp = []
        temp = temp + multarrs
        temp.append(weekarr)
        results = self.check_future_week_limits(temp, num_pos)
        # countam = 0
        # countpm = 0
        for i in results:
            amlim, pmlim = i
            # print(i)
            if amlim or pmlim:
                # if amlim:
                #     countam += 1
                # if pmlim:
                #     countpm += 1
                # print(countam,countpm)
                # print("the new week chosen breaks limits")
                return True

        return False

    def reached_week_lim(self, arr, num_pos):

        temp = self.check_week_limits(arr, num_pos)

        # print("limits reached for the week by day (AM/PM): " + str(temp))
        countam = 0
        countpm = 0

        for i in temp:
            am, pm = i
            # print(am)
            # print(pm)
            if am:
                countam += 1
                # print(countam)
            if pm:
                countpm += 1
                # print(countam)

        if countam >= 7 and countpm >= 7:
            return True

        return False

    def reached_restrict_week_lim(self, arr, num_pos):
        temp = self.check_week_limits(arr, num_pos)
        countam = 0
        countpm = 0

        for i in temp:
            am, pm = i
            if am:
                countam += 1
            if pm:
                countpm += 1

        # print(countam, countpm)
        if countam >= 2 and countpm >= 2:
            return True

        return False

    def remove_over_lim_weeks(self, options, num_pos, arr):
        limits = self.check_week_limits(arr, num_pos)
        temp = []
        temp = temp + options
        # print(limits)
        for i in range(len(limits)):
            amover, pmover = limits[i]

            if amover:
                temp = self.remove_over_lim_shift(temp, i, 1)

            if pmover:
                temp = self.remove_over_lim_shift(temp, i, 2)

        return temp

    def remove_over_lim_shift(self, options, day, time):
        temp = []
        temp = temp + options
        toremove = []
        for i in temp:
            if i[day] == time:
                toremove.append(i)

        # print("number if templates needing to be removed because they breach the limits: " + str(len(toremove)))
        for j in toremove:
            temp.remove(j)

        # print("new number of templates after limits breachers removed: " + str(len(temp)))
        return temp

    def min_workdays_restrict(self, options, numdays):
        temp = []
        temp = temp + options
        toremove = []
        for i in temp:
            counton = 0
            for j in i:
                if j > 0:
                    counton += 1

            if counton > numdays or counton < numdays:
                toremove.append(i)

        for k in toremove:
            temp.remove(k)

        return temp

    def possible_to_cont(self, arr, num_pos):
        temp = self.check_week_limits(arr, num_pos)
        for i in temp:
            amlim, pmlim = i
            # print(i)
            if amlim or pmlim:
                return False

        return True

    def num_of_lim_reached(self, schedarr, num_pos):
        temp = []
        temp = temp + self.check_week_limits(schedarr, num_pos)
        count = 0
        for i in temp:
            am, pm = i
            if am and pm:
                count += 1

        return count

    # TODO create biweek week 2 eliminator

    # TODO create biweek week 1 eliminator

    # TODO create generator that is no longer arbitary until the end. Just create all the possible options and then parse
    #  through them like you have already been doing fuck ram limits it wont even be that much. Worst case you have to
    #   use numpy again BUT DO NOT RELY ON IT. DO WHATEVER YOU CAN WITHOUT IT FIRST. It should only be used as an
    #    optimization step

#-------------------below generative function still broken--------------------------------------------------------------
    #FUCK MY LIFE (but at least the solution this led me to will be quick)

    def gen_week_sched_v2(self, num_pos, section):

        assert num_pos >= 2, "you seriously couldn't handle less than 2 positions on your own? if you need a little help use the single template generator functions..."
        week1sched = []
        week2sched = []
        fullrestr = self.full_restriction(section).copy()
        week1opts = self.full_restriction(section).copy()
        week2opts = self.full_restriction(section).copy()
        week1temp = week1opts[rand.randrange(0, len(week1opts)-1)].copy()
        week2opts = self.week2_eliminator(week2opts, week1temp[0], week1temp[len(week1temp)-1]).copy()
        week2temp = week2opts[rand.randrange(0, len(week2opts)-1)].copy()
        week1sched.append(week1temp)
        week2sched.append(week2temp)
        week1temp = week1opts[rand.randrange(0, len(week1opts)-1)].copy()
        week2opts = self.week2_eliminator(fullrestr, week1temp[0], week1temp[len(week1temp)-1]).copy()
        week2temp = week2opts[rand.randrange(0, len(week2opts)-1)].copy()
        week1sched.append(week1temp.copy())
        week2sched.append(week2temp.copy())
        week1opts = self.full_restriction(section).copy()
        week2opts = self.full_restriction(section).copy()


        #num_people = num_pos * 4

        if self.debug:
            print("week 1 starting options: " + str(len(week1opts)))
            print("week 2 starting options: " + str(len(week2opts)))
            print(self.reached_week_lim(week1sched, num_pos), self.reached_week_lim(week2sched, num_pos))

        while not self.reached_week_lim(week1sched, num_pos) and not self.reached_week_lim(week2sched, num_pos):
            maxworkdayav1 = 7
            maxworkdayav2 = 7
            week2opts = week2opts + self.full_restriction(section).copy()
            # print("running creation loop")

            # print(self.possible_to_cont(week1sched, num_pos), self.possible_to_cont(week2sched, num_pos))

            # if not self.possible_to_cont(week1sched, num_pos) and not self.possible_to_cont(week2sched, num_pos):
            #     print("all values have limits/parameters have been met impossible to continue; re-evaluate (1)")
            #     break
            if self.debug:
                print("Options available for week 1: " + str(len(week1opts)))
                print("Options available for week 2: " + str(len(week2opts)))

            if self.reached_restrict_week_lim(week1sched, num_pos):
                # print("restricted limits reached for week 1")
                maxworkdayav1 -= self.num_of_lim_reached(week1sched, num_pos)
                if maxworkdayav1 <= 0:
                    print("no more options available in week 1, impossible to continue; re-valuate (2)")
                    break
                week1opts = week1opts + self.min_workdays_restrict(self.max_hours_restrict(section), maxworkdayav1).copy()
                week1opts = self.remove_over_lim_weeks(week1opts, num_pos, self.check_week_limits(week1sched, num_pos)).copy()
                # print(len(week1opts))

            if len(week1opts) <= 0:
                print("there are no options available for week 1 that meet any parameters (1)")
                break

            week1temp = week1opts[rand.randrange(0, len(week1opts)-1)].copy()

            if self.reached_restrict_week_lim(week2sched, num_pos):
                # print("restricted limits reached for week 2")
                maxworkdayav2 -= self.num_of_lim_reached(week2sched, num_pos)
                if maxworkdayav2 <= 0:
                    print("no more options available in week 2, impossible to continue; re-evaluate (3)")
                    break
                week2opts = week2opts + self.min_workdays_restrict(self.max_hours_restrict(section), maxworkdayav2).copy()
                week2opts = self.remove_over_lim_weeks(week2opts, num_pos, self.check_week_limits(week1sched, num_pos)).copy()
                # print(len(week2opts))

            week2opts = self.week2_eliminator(week2opts, week1temp[0], week2temp[len(week1temp)-1]).copy()

            if len(week2opts) <= 0:
                print("no more options available for week 2 that meet any parameters (2)")
                break


            week2temp = week2opts[rand.randrange(0, len(week2opts)-1)].copy()


            # print(self.new_week_over_lim(week1sched, week1temp, num_pos), self.new_week_over_lim(week2sched, week2temp, num_pos))

            #below condintional is purposeless because as soon as any limit is breached it returns false
            # if self.new_week_over_lim(week1sched, week1temp, num_pos) and self.new_week_over_lim(week2sched, week2temp, num_pos):
            #     print("the week picked breaks limits/parameters; re-evaluate (4)")
            #     # print(week1temp, week2temp)
            #     break

            if self.reached_week_lim(week1sched, num_pos) and self.reached_week_lim(week2sched, num_pos):
                print("it is impossible to continue limits/parameters broken; re-evaluate(5)")
                break

            # print(week1temp, week2temp)
            week1sched.append(week1temp.copy())
            week2sched.append(week2temp.copy())

            # print(len(week1sched), len(week2sched))
            # print(self.reached_week_lim(week1sched, num_pos), self.reached_week_lim(week2sched, num_pos))

            if self.reached_week_lim(week1sched, num_pos) and self.reached_week_lim(week2sched, num_pos):
                print("it is impossible to continue limits/parameters broken; re-evaluate(6)")
                break

        # print(self.reached_week_lim(week1sched, num_pos), self.reached_week_lim(week2sched, num_pos))

        schedarr = self.bridge_weeks(week1sched, week2sched).copy()
        print(len(schedarr))
        return schedarr

    def gen_week_sched_v2_self(self, num_pos):
        temp = self.to_num_arr_int()
        temp = self.gen_week_sched_v2(num_pos, temp)
        return temp
#-----above method still does not work... no matter how I try it seems arbitrary despite it being random only at the bar minimum-----


    def biweekly_perms(self, options):
        temp = options.copy()
        temp = self.max_hours_restrict(temp)
        newarr = []
        for i in temp:
            temp2 = temp.copy()
            temp2 = self.week2_eliminator(temp2, i[0], i[len(i)-1])
            for j in temp2:
                temp3 = i.copy() + j.copy()
                newarr.append(temp3)
                temp3 = j.copy() + i.copy()
                newarr.append(temp3)

        print(len(newarr))
        return newarr

    def biweekly_perms_self(self):
        return self.biweekly_perms(self.to_num_arr_int())


#--------------------------------------------------- single genereative functions below --------------------------------

    def gen_1_week(self, section):

        week1opts = self.full_restriction(section).copy()
        week1temp = week1opts[rand.randrange(0, len(week1opts)-1)].copy()

        # week1opts = self.max_hours_restrict(section)

        # print("week 1 options: " + str(week1opts))
        return np.array(week1temp)

    def gen_1_week_self(self):
        temp = self.gen_1_week(self.to_num_arr_int())
        return temp



    def gen_1_biweek(self, section):
        week1opts =self.full_restriction(section).copy()
        week1temp = week1opts[rand.randrange(0, len(week1opts)-1)].copy()

        week2opts = self.week2_eliminator(self.full_restriction(section), week1temp[0], week1temp[len(week1temp)-1]).copy()
        week2temp = week2opts[rand.randrange(0, len(week2opts)-1)].copy()

        sched = week1temp + week2temp

        return np.array(sched)

    def gen_1_biweek_self(self):
        temp = self.gen_1_biweek(self.to_num_arr_int())
        return temp


# ------------------------------------------by n weeks instead of 1 week starts below -------------------------------

    def day_off_max_restrict_n_weeks(self, list):
        temp = list
        toremove = []
        for i in temp:
            countoff = 0
            # print(i)
            for j in i:
                if j == 0:
                    # print("another day off counted")
                    countoff += 1
                    # print(countoff)
                if countoff > (2 * int(self.get_depth()/7)):
                    # print("removing week template")
                    toremove.append(i)
                    break
        # print("number of weeks being removed: " + str(len(toremove)))
        for i in toremove:
            temp.remove(i)

        # print("new number of templates: " + str(len(temp)))
        return temp

    def day_off_max_restrict_self_n_weeks(self):
        temp = self.to_num_arr_int()
        # print(len(temp))
        temp = self.day_off_max_restrict_n_weeks(temp)
        # print(len(temp))
        return temp

    def day_off_min_restrict_n_weeks(self, list):
        temp = list
        toremove = []
        for i in temp:
            countoff = 0
            # print(i)
            for j in i:
                if j == 0:
                    # print("another day off counted")
                    countoff += 1
                    # print(countoff)

            if countoff < (2 * int(self.get_depth()/7)):
                # print("removing week template")
                toremove.append(i)
        # print("number of weeks being removed: " + str(len(toremove)))
        for i in toremove:
            temp.remove(i)

        # print("new number of templates: " + str(len(temp)))
        return temp

    def day_off_min_restrict_self_n_weeks(self):
        temp = self.to_num_arr_int()
        temp = self.day_off_min_restrict_n_weeks(temp)
        return temp

    def only_5_wrk_days_n_weeks(self, list):
        temp = self.day_off_max_restrict_n_weeks(list)
        temp = self.day_off_min_restrict_n_weeks(temp)
        return temp

    def only_5_wrk_days_self_n_weeks(self):
        temp = self.to_num_arr_int()
        temp = self.only_5_wrk_days_n_weeks(temp)
        return temp

    def no_clopens_n_weeks(self, section):
        temp = section
        toremove = []
        for i in temp:
            prevval = 0
            # print(i)
            for j in i:
                currval = j
                # print("currval = " + str(currval))
                # print("prevval = " + str(prevval))
                if currval == 1 and prevval == 2:
                    # print("found a clopen!")
                    toremove.append(i)
                    break
                prevval = j

        # print("number of weeks being removed: " + str(len(toremove)))
        for i in toremove:
            temp.remove(i)

        # print("new number of templates: " + str(len(temp)))

        return temp

    def no_clopens_self_n_weeks(self):
        temp = self.to_num_arr_int()
        temp = self.no_clopens_n_weeks(temp)
        return temp

    def full_restriction_n_weeks(self, section):
        temp = section
        temp = self.only_5_wrk_days_n_weeks(temp)
        temp = self.no_clopens_n_weeks(temp)
        return temp

    def full_restriction_self_n_weeks(self):
        temp = self.to_num_arr_int()
        temp = self.full_restriction_n_weeks(temp)
        return temp


class PermutationNode(object):
    debug = False
    currval = 0
    depth = 0
    parent = None
    nextvaloff = None
    nextvalam = None
    nextvalpm = None

    def __init__(self, depth, currval, depthlim, parent):
        self.depth = depth
        self.parent = parent
        self.currval = currval
        if depth+1 <= depthlim:
            self.nextvaloff = PermutationNode(self.depth+1, currval=0, depthlim=depthlim, parent=self)
            self.nextvalam = PermutationNode(self.depth+1, currval=1, depthlim=depthlim, parent=self)
            self.nextvalpm = PermutationNode(self.depth+1, currval=2, depthlim=depthlim, parent=self)

        if self.debug:
            print(self.nextvaloff)
            print(self.nextvalam)
            print(self.nextvalpm)

    def get_nextoff(self):
        """
        :return: value of next day (off-day/0)
        """
        return self.nextvaloff

    def get_nextam(self):
        """
        :return: value of next day (am/1)
        """
        return self.nextvalam

    def get_nextpm(self):
        """
        :return: value of next day (pm/2)
        """
        return self.nextvalpm

    def get_parent(self):
        return self.parent

    def set_nextam(self, newam):
        self.nextvalam = newam

    def set_nextpm(self, newpm):
        self.nextvalpm = newpm

    def set_nextoff(self, newoff):
        self.nextvaloff = newoff


    def __str__(self):
        return str(self.currval)

    def back_prop_recurs(self):
        if self.parent == None:
            return str(self)
        temp = str(self) + "," + self.parent.back_prop_recurs()
        return temp

    def forward_prop_recurs(self):
        if self.nextvaloff == None:
            return self.back_prop_recurs()

        return self.nextvaloff.forward_prop_recurs() + " \n " + self.nextvalam.forward_prop_recurs() + " \n " + self.nextvalpm.forward_prop_recurs() #+" \n "


