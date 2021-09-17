# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
import datetime


from logapp.models import *

# Remember to change these when the experiment terms change in the
# Prolog code.
term2string = {
    1 : "males",
    2 : "females",
    3 : "adults",
    4 : "mothers",
    5 : "fathers",
    6 : "parents",
    7 : "students",
    8 : "teachers",
    9 : "doctors",
}    

# Remember to change these when the experiment terms change in the
# Prolog code (test2015b)
artificialterm2string = {
    1 : "bloogs",
    2 : "zeefs",
    3 : "kloojarbs",
    4 : "flarkjerbs",
    5 : "greegarfs",
    6 : "habzoops",
    7 : "plarfeebs",
    8 : "meefjarbs",
    9 : "troofklejoobs",
}    

def root_view(request):
    return HttpResponseRedirect('/test2019/') # Just redirect

def getValue(request, key, bValid):
    if not bValid:
        return (None, False)
    else:
        if key in request.GET:
            value = request.GET[key]
            return (value, True)
        else:
            return (None, False)
    

def log(request):
    if request.method == "GET":
        bValid = True
        (usernumber_str, bValid) = getValue(request, u"uid", bValid)
        (timelapse_str, bValid) = getValue(request, u"timelapse", bValid)
        (syllnumber_str, bValid) = getValue(request, u"syllnumber", bValid)
        (figure_str, bValid) = getValue(request, u"figure", bValid)
        (correctness_str, bValid) = getValue(request, u"corr", bValid)
        (term_S_str, bValid) = getValue(request, u"S", bValid)
        (term_M_str, bValid) = getValue(request, u"M", bValid)
        (term_P_str, bValid) = getValue(request, u"P", bValid)
        (conclusion_truth_value_str, bValid) = getValue(request, u"conclusion", bValid)

        if not bValid:
            return render(request, 'log.html')
        else:
            if correctness_str == "true":
                bCorrect = True
            else:
                bCorrect = False

            if conclusion_truth_value_str == "1":
                bConclusionTruthValue = True
            else:
                bConclusionTruthValue = False

            newobj = Answer(usernumber=int(usernumber_str),
                            timelapse=int(timelapse_str),
                            syllnumber=int(syllnumber_str),
                            figure=int(figure_str),
                            correctness=bCorrect)
            newobj.save()


            newobj2 = Answer2(answer=newobj,
                              conclusion_truth_value=bConclusionTruthValue,
                              term_S=int(term_S_str),
                              term_M=int(term_M_str),
                              term_P=int(term_P_str))
            newobj2.save()

            return render(request, 'log.html')
    else:
        return render(request, 'log.html')

def log3(request):
    if request.method == "GET":
        bValid = True
        (usernumber_str, bValid) = getValue(request, u"uid", bValid)
        (timelapse_str, bValid) = getValue(request, u"timelapse", bValid)
        (propkind_str, bValid) = getValue(request, u"propkind", bValid)
        (figure_str, bValid) = getValue(request, u"figure", bValid)
        (correctness_str, bValid) = getValue(request, u"corr", bValid)
        (term_S_str, bValid) = getValue(request, u"S", bValid)
        (term_M_str, bValid) = getValue(request, u"M", bValid)
        (term_P_str, bValid) = getValue(request, u"P", bValid)
        (term_Q1_str, bValid) = getValue(request, u"q1", bValid)
        (term_Q2_str, bValid) = getValue(request, u"q2", bValid)
        (term_Q3_str, bValid) = getValue(request, u"q3", bValid)
        (conclusion_truth_value_str, bValid) = getValue(request, u"conclusion", bValid)
        (validity_answer, bValid) = getValue(request, u"validity", bValid)

        if not bValid:
            return render(request, 'log.html')
        else:
            if correctness_str == "true":
                bCorrect = True
            else:
                bCorrect = False

            if conclusion_truth_value_str == "1":
                bConclusionTruthValue = True
            else:
                bConclusionTruthValue = False

            newobj3 = Answer3(usernumber=int(usernumber_str),
                              timelapse=int(timelapse_str),
                              figure=int(figure_str),
                              quantor_1=term_Q1_str,
                              quantor_2=term_Q2_str,
                              quantor_3=term_Q3_str,
                              term_S=int(term_S_str),
                              term_M=int(term_M_str),
                              term_P=int(term_P_str),
                              propkind=propkind_str,
                              student_answer=validity_answer,
                              correctness=bCorrect,
                              conclusion_truth_value=bConclusionTruthValue)

            newobj3.save()

            return render(request, 'log.html')
    else:
        return render(request, 'log.html')

def log5(request):
    """log5 is a version of log3 without conclusion. It is meant for
    the version that has artificial words as terms in the syllogism."""
    if request.method == "GET":
        bValid = True
        (usernumber_str, bValid) = getValue(request, u"uid", bValid)
        (timelapse_str, bValid) = getValue(request, u"timelapse", bValid)
        (propkind_str, bValid) = getValue(request, u"propkind", bValid)
        (figure_str, bValid) = getValue(request, u"figure", bValid)
        (correctness_str, bValid) = getValue(request, u"corr", bValid)
        (term_S_str, bValid) = getValue(request, u"S", bValid)
        (term_M_str, bValid) = getValue(request, u"M", bValid)
        (term_P_str, bValid) = getValue(request, u"P", bValid)
        (term_Q1_str, bValid) = getValue(request, u"q1", bValid)
        (term_Q2_str, bValid) = getValue(request, u"q2", bValid)
        (term_Q3_str, bValid) = getValue(request, u"q3", bValid)
        (validity_answer, bValid) = getValue(request, u"validity", bValid)

        if not bValid:
            return render(request, 'log.html')
        else:
            if correctness_str == "true":
                bCorrect = True
            else:
                bCorrect = False

            bConclusionTruthValue = False

            newobj5 = Answer5(usernumber=int(usernumber_str),
                              timelapse=int(timelapse_str),
                              figure=int(figure_str),
                              quantor_1=term_Q1_str,
                              quantor_2=term_Q2_str,
                              quantor_3=term_Q3_str,
                              term_S=int(term_S_str),
                              term_M=int(term_M_str),
                              term_P=int(term_P_str),
                              propkind=propkind_str,
                              student_answer=validity_answer,
                              correctness=bCorrect,
                              conclusion_truth_value=bConclusionTruthValue)

            newobj5.save()

            return render(request, 'log.html')
    else:
        return render(request, 'log.html')

def log4(request):
    if request.method == "GET":
        bValid = True
        (usernumber_str, bValid) = getValue(request, u"uid", bValid)
        (timelapse_str, bValid) = getValue(request, u"timelapse", bValid)
        (figure_str, bValid) = getValue(request, u"figure", bValid)
        (term_Q1_str, bValid) = getValue(request, u"q1", bValid)
        (term_Q2_str, bValid) = getValue(request, u"q2", bValid)
        (term_Q3_str, bValid) = getValue(request, u"q3", bValid)
        (correctness_str, bValid) = getValue(request, u"corr", bValid)
        (term_S_str, bValid) = getValue(request, u"S", bValid)
        (term_M_str, bValid) = getValue(request, u"M", bValid)
        (term_P_str, bValid) = getValue(request, u"P", bValid)
        (conclusion_truth_value_str, bValid) = getValue(request, u"conclusion", bValid)
        (validity_answer, bValid) = getValue(request, u"validity", bValid)
        (rule_clicks_str, bValid) = getValue(request, u"rule_clicks", bValid)

        if not bValid:
            return render(request, 'log.html')
        else:
            if correctness_str == "true":
                bCorrect = True
            else:
                bCorrect = False

            if conclusion_truth_value_str == "1":
                bConclusionTruthValue = True
            else:
                bConclusionTruthValue = False

            try:
                rule_clicks = int(rule_clicks_str)
            except:
                rule_clicks = -1

            propkind_str = "verbal"

            newobj4 = Answer4(usernumber=int(usernumber_str),
                              timelapse=int(timelapse_str),
                              figure=int(figure_str),
                              quantor_1=term_Q1_str,
                              quantor_2=term_Q2_str,
                              quantor_3=term_Q3_str,
                              term_S=int(term_S_str),
                              term_M=int(term_M_str),
                              term_P=int(term_P_str),
                              propkind=propkind_str,
                              student_answer=validity_answer,
                              correctness=bCorrect,
                              conclusion_truth_value=bConclusionTruthValue,
                              rule_clicks=rule_clicks)

            newobj4.save()

            return render(request, 'log.html')
    else:
        return render(request, 'log.html')

def getCorrectness(result, usernumber, date, figure, syllnumber):
    if date not in result:
        return (0,0)
    if usernumber not in result[date]:
        return (0,0)
    if figure not in result[date][usernumber]:
        return (0,0)
    if syllnumber not in result[date][usernumber][figure]:
        return (0,0)
    correct = 0
    wrong = 0
    if "correct" in result[date][usernumber][figure][syllnumber]:
        correct = result[date][usernumber][figure][syllnumber]["correct"]
    if "wrong" in result[date][usernumber][figure][syllnumber]:
        wrong = result[date][usernumber][figure][syllnumber]["wrong"]
    return (correct, wrong)

def dump(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/test2018/')
    else:
        import csv
        from django.http import HttpResponse

        answer_list = list(Answer.objects.all())
        
        result = {} # date --> { usernumber --> { figure --> {syllnumber --> { "correct" : correct-count, "wrong" : wrong-count } } } }
        
        for answer in answer_list:
            date = u"%s" % answer.date

            result.setdefault(date, {})



            result[date].setdefault(answer.usernumber, {})

            result[date][answer.usernumber].setdefault(answer.figure, {})

            result[date][answer.usernumber][answer.figure].setdefault(answer.syllnumber, {})

            result[date][answer.usernumber][answer.figure][answer.syllnumber].setdefault("correct", 0)
            result[date][answer.usernumber][answer.figure][answer.syllnumber].setdefault("wrong", 0)

            if answer.correctness:
                result[date][answer.usernumber][answer.figure][answer.syllnumber]["correct"] += 1
            else:
                result[date][answer.usernumber][answer.figure][answer.syllnumber]["wrong"] += 1

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse("", content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=logsyllog-data.csv'

    writer = csv.writer(response)
    first_row = ['date', 'usernumber']
    for figure in [1,2,3,4]:
        for syllnumber in [1,2,3,4,5,6,7,8,9,10,11,12]:
            first_row.append('F:%d/S:%d:C' % (figure, syllnumber))
            first_row.append('F:%d/S:%d:W' % (figure, syllnumber))
    writer.writerow(first_row)
    
    for date in sorted(result):
        for usernumber in sorted(result[date]):
            next_row = []
            next_row.append(date)
            next_row.append('%d' % usernumber)
            for figure in [1,2,3,4]:
                for syllnumber in [1,2,3,4,5,6,7,8,9,10,11,12]:
                    (correct,wrong) = getCorrectness(result, usernumber, date, figure, syllnumber)
                    next_row.append('%d' % correct)
                    next_row.append('%d' % wrong)
            writer.writerow(next_row)
            del next_row

    return response




        
def dump2(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/test2018/')
    else:
        import csv
        from django.http import HttpResponse

        answer_list = Answer2.objects.all().order_by("id")
        
        result = {} # date --> { order --> { mydict } } 

        order_dict = {} #usernumber --> order-int

        order_int = 0
        
        for answer2 in answer_list:
            answer = answer2.answer
            date = u"%s" % answer.date
            usernumber = answer.usernumber
            figure = answer.figure
            syllnumber = answer.syllnumber
            timelapse = answer.timelapse
            correctness = answer.correctness

            conclusion_truth_value = answer2.conclusion_truth_value
            term_S = term2string[answer2.term_S]
            term_M = term2string[answer2.term_M]
            term_P = term2string[answer2.term_P]

            if usernumber in order_dict:
                order = order_dict[usernumber]
            else:
                order = order_int
                order_int += 1
                order_dict[usernumber] = order

            result.setdefault(date, {})
            result[date].setdefault(order, [])

            result[date][order].append({
                    "usernumber" : usernumber,
                    "figure" : figure,
                    "syllnumber" : syllnumber,
                    "timelapse" : timelapse,
                    "correctness" : correctness,
                    "conclusion_truth_value" : conclusion_truth_value,
                    "term_S" : term_S,
                    "term_M" : term_M,
                    "term_P" : term_P,
                    })


    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse("", content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=logsyllog-data.csv'

    writer = csv.writer(response)
    first_row = ['date', 'usernumber', 'figure', 'syllnumber', 'term_S', 'term_M', 'term_P', 'correctness', 'conclusion', 'timelapse (s)', 'totaltime (s)', 'lastcorrectinarow', 'answercount']
    writer.writerow(first_row)
    
    for date in sorted(result):
        for order in sorted(result[date]):
            usernumber = 0
            last_correct_in_a_row = 0
            totaltime = 0
            answercount = 0
            for mydict in result[date][order]:
                answercount += 1
                next_row = []
                next_row.append(date)
                next_row.append('%d' % mydict['usernumber'])
                usernumber = mydict['usernumber']
                next_row.append('%d' % mydict['figure'])
                next_row.append('%d' % mydict['syllnumber'])
                next_row.append('%s' % mydict['term_S'])
                next_row.append('%s' % mydict['term_M'])
                next_row.append('%s' % mydict['term_P'])
                next_row.append('%s' % mydict['correctness'])
                next_row.append('%s' % mydict['conclusion_truth_value'])
                next_row.append('%.3f' % ((1.0 * mydict['timelapse']) / 1000.0))
                totaltime += mydict['timelapse']
                writer.writerow(next_row)
                del next_row

                if mydict["correctness"]:
                    last_correct_in_a_row += 1
                else:
                    last_correct_in_a_row = 0
                    
            next_row = [date, '%d' % usernumber, '', '', '', '', '', '', '', '', '%.3f' % ((1.0 * totaltime) / 1000.0), '%d' % last_correct_in_a_row, '%d' % answercount]
            writer.writerow(next_row)
            del next_row

    return response

# Amended from: http://docs.python.org/2/library/datetime.html
class GMT1(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=1) + self.dst(dt)
    def dst(self, dt):
        # DST starts last Sunday in March
        d = datetime.datetime(dt.year, 4, 1)   # ends last Sunday in October
        self.dston = d - datetime.timedelta(days=d.weekday() + 1)
        d = datetime.datetime(dt.year, 11, 1)
        self.dstoff = d - datetime.timedelta(days=d.weekday() + 1)
        if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
            return datetime.timedelta(hours=1)
        else:
            return datetime.timedelta(0)
    def tzname(self,dt):
        return "GMT +1"

session_start_dict = {
    "2014-02-04" : 12,
    "2014-02-05" : 12,
    "2014-02-06" : 12,
    "2014-02-07" : 10,
}

def fake_timezone1(last_time, time, date):
    if date not in session_start_dict:
        return time
    else:
        session_start = session_start_dict[date]

        hour = int(time[0:2])

        if hour < session_start:
            hour += 6 # Assume UTC-0500
            new_time = "%02d:%s" % (hour, time[3:])
            return new_time
        else:
            return time
    

def fake_timezone2(last_time, time, date):
    if date not in session_start_dict:
        return time
    elif last_time == None:
        return time
    else:
        hour_minute = time[0:5]
        last_hour_minute = last_time[0:5]

        if hour_minute < last_hour_minute:
            hour = int(time[0:2])
            hour += 1
            new_time = "%02d:%s" % (hour, time[3:])
            return new_time
        else:
            return time

def dump3(request):
    bAggregateSessions = False
    return dump3_super(request, bAggregateSessions)
        
def dump3_aggregatesess(request):
    bAggregateSessions = True
    return dump3_super(request, bAggregateSessions)
        

def dump3_super(request, bAggregateSessions):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/test2018/')
    else:
        import csv
        from django.http import HttpResponse

        answer_list = Answer3.objects.all().order_by("id")
        
        result = {} # date --> { order --> { mydict } } 

        order_dict = {} #usernumber --> order-int

        order_int = 0

        mytz = GMT1()
        
        for answer3 in answer_list:
            usernumber = answer3.usernumber

            # Convert aware datetime into our own timezone
            mydate = answer3.date
            date = (u"%s" % mydate)[0:10]
            time = (u"%s" % mydate)[11:19]

            timelapse = answer3.timelapse

            figure = answer3.figure
            quantor_1 = answer3.quantor_1
            quantor_2 = answer3.quantor_2
            quantor_3 = answer3.quantor_3

            term_S = term2string[answer3.term_S]
            term_M = term2string[answer3.term_M]
            term_P = term2string[answer3.term_P]

            correctness = answer3.correctness
            conclusion_truth_value = answer3.conclusion_truth_value
            student_answer = answer3.student_answer
            propkind = answer3.propkind

            if student_answer == "valid":
                if correctness:
                    syllogism_validity = "valid"
                else:
                    syllogism_validity = "invalid"
            else:
                if correctness:
                    syllogism_validity = "invalid"
                else:
                    syllogism_validity = "valid"

            if usernumber in order_dict:
                order = order_dict[usernumber]
            else:
                order = order_int
                order_int += 1
                order_dict[usernumber] = order

            result.setdefault(date, {})
            result[date].setdefault(order, [])

            result[date][order].append({
                "time" : time,
                "usernumber" : usernumber,
                "timelapse" : timelapse,
                
                "figure" : figure,
                "quantor_1" : quantor_1,
                "quantor_2" : quantor_2,
                "quantor_3" : quantor_3,

                "term_S" : term_S,
                "term_M" : term_M,
                "term_P" : term_P,
                
                "correctness" : correctness,
                "syllogism_validity" : syllogism_validity,
                "conclusion_truth_value" : conclusion_truth_value,
                "student_answer" : student_answer,
                "propkind" : propkind,
            })


    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse("", content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=logsyllog-data3.csv'

    writer = csv.writer(response)
    if not bAggregateSessions:
        first_row = ['date', 'time', 'usernumber', 'figure', 'quantor_1', 'quantor_2', 'quantor_3', 'term_S', 'term_M', 'term_P', 'conclusion_truth_value', 'syllogism_validity',  'answer_is_correct', 'answer', 'propkind', 'timelapse (s)', 'totaltime (s)', 'lastcorrectinarow', 'answercount', 'correctanswercount']
    else:
        first_row = ['date', 'usernumber', 'totaltime (s)', 'lastcorrectinarow', 'answercount', 'correctanswercount']

    writer.writerow(first_row)
    for date in sorted(result):
        for order in sorted(result[date]):
            usernumber = 0
            last_correct_in_a_row = 0
            totaltime = 0
            answercount = 0
            correctanswercount = 0
            for mydict in result[date][order]:
                answercount += 1
                next_row = []
                next_row.append(date)
                next_row.append('%s' % mydict['time'])
                next_row.append('%d' % mydict['usernumber'])
                usernumber = mydict['usernumber']
                next_row.append('%d' % mydict['figure'])
                next_row.append('%s' % mydict['quantor_1'])
                next_row.append('%s' % mydict['quantor_2'])
                next_row.append('%s' % mydict['quantor_3'])
                next_row.append('%s' % mydict['term_S'])
                next_row.append('%s' % mydict['term_M'])
                next_row.append('%s' % mydict['term_P'])
                next_row.append('%s' % mydict['conclusion_truth_value'])
                next_row.append('%s' % mydict['syllogism_validity'])
                next_row.append('%s' % mydict['correctness'])
                next_row.append('%s' % mydict['student_answer'])
                next_row.append('%s' % mydict['propkind'])
                next_row.append('%.3f' % ((1.0 * mydict['timelapse']) / 1000.0))
                totaltime += mydict['timelapse']
                if not bAggregateSessions:
                    writer.writerow(next_row)
                    del next_row

                if mydict["correctness"]:
                    last_correct_in_a_row += 1
                    correctanswercount += 1
                else:
                    last_correct_in_a_row = 0

            if not bAggregateSessions:
                next_row = [date, '', '%d' % usernumber, '', '', '', '', '', '', '', '', '', '', '', '', '', '%.3f' % ((1.0 * totaltime) / 1000.0), '%d' % last_correct_in_a_row, '%d' % answercount, '%d' % correctanswercount]
            else:
                next_row = [date, '%d' % usernumber, '%.3f' % ((1.0 * totaltime) / 1000.0), '%d' % last_correct_in_a_row, '%d' % answercount, '%d' % correctanswercount]
            writer.writerow(next_row)
            del next_row

    return response

def getSyllogismName(figure, quantor_1, quantor_2, quantor_3):
    return u"%d:%s%s%s" % (figure, quantor_1[0], quantor_2[0], quantor_3[0])

def dump3_syllogism_based_validonly(request):
    bDoValidSyllogismsOnly = True
    start_date = None
    end_date = None
    return dump3_syllogism_based_super(request, bDoValidSyllogismsOnly, start_date, end_date)

def dump3_syllogism_based_validonly_dates(request, start_date, end_date):
    bDoValidSyllogismsOnly = True
    return dump3_syllogism_based_super(request, bDoValidSyllogismsOnly, start_date, end_date)

def dump3_syllogism_based_valid_and_invalid(request):
    bDoValidSyllogismsOnly = False
    start_date = None
    end_date = None
    return dump3_syllogism_based_super(request, bDoValidSyllogismsOnly, start_date, end_date)

def dump3_syllogism_based_valid_and_invalid_dates(request, start_date, end_date):
    bDoValidSyllogismsOnly = False
    return dump3_syllogism_based_super(request, bDoValidSyllogismsOnly, start_date, end_date)

def dump3_syllogism_based_super(request, bDoValidSyllogismsOnly, start_date, end_date):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/test2018/')
    else:
        import csv
        from django.http import HttpResponse

        answer_list = Answer3.objects.all().order_by("id")
        
        result = {} # date --> { syllogism_name --> { mydict } } 

        mytz = GMT1()

        if start_date == None and end_date == None:
            bDoDate = True
        else:
            bDoDate = False
            
        for answer3 in answer_list:
            usernumber = answer3.usernumber

            # Convert aware datetime into our own timezone
            mydate = answer3.date
            date = (u"%s" % mydate)[0:10]
            time = (u"%s" % mydate)[11:19]

            if bDoDate:
                real_date = date
            else:
                bDoDate = False
                if date >= start_date and date <= end_date:
                    pass
                else:
                    continue
                real_date = "0000-00-00"

            timelapse = answer3.timelapse

            figure = answer3.figure
            quantor_1 = answer3.quantor_1
            quantor_2 = answer3.quantor_2
            quantor_3 = answer3.quantor_3

            syllogism_name = getSyllogismName(figure, quantor_1, quantor_2, quantor_3)

            correctness = answer3.correctness
            conclusion_truth_value = answer3.conclusion_truth_value
            student_answer = answer3.student_answer
            propkind = answer3.propkind

            if student_answer == "valid":
                if correctness:
                    syllogism_validity = "valid"
                else:
                    syllogism_validity = "invalid"
            else:
                if correctness:
                    syllogism_validity = "invalid"
                else:
                    syllogism_validity = "valid"

            if bDoValidSyllogismsOnly:
                if syllogism_validity == "valid":
                    bDoIt = True
                else:
                    bDoIt = False
            else:
                bDoIt = True

            if bDoIt:
                result.setdefault(real_date, {})
                result[real_date].setdefault(syllogism_name, {
                    "question_count" : 0,
                    "correct_count" : 0,
                    "validity" : syllogism_validity,
                })

                result[real_date][syllogism_name]["question_count"] += 1
                if correctness:
                    result[real_date][syllogism_name]["correct_count"] += 1


    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse("", content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=logsyllog-data3-syllogism_based.csv'

    writer = csv.writer(response)
    if bDoDate:
        first_row = ['date', 'syl_name', 'validity', 'question_count', 'correct_count']
        writer.writerow(first_row)
    else:
        first_row = ['date_range', 'syl_name', 'validity', 'question_count', 'correct_count']
        writer.writerow(first_row)
        
        
    for date in sorted(result):
        for syllogism_name in sorted(result[date]):
            question_count = result[date][syllogism_name]["question_count"]
            correct_count = result[date][syllogism_name]["correct_count"]
            validity = result[date][syllogism_name]["validity"]
            next_row = []
            if bDoDate:
                next_row.append(date)
            else:
                if start_date == end_date:
                    next_row.append("%s" % start_date)
                else:
                    next_row.append("%s-%s" % (start_date, end_date))
            next_row.append(syllogism_name)
            next_row.append(validity)
            next_row.append('%d' % question_count)
            next_row.append('%d' % correct_count)
            writer.writerow(next_row)
            del next_row

    return response

def dump4(request):
    bAggregateSessions = False    
    return dump4_super(request, bAggregateSessions)
    
def dump4_aggregatesess(request):
    bAggregateSessions = True
    return dump4_super(request, bAggregateSessions)
    
def dump4_super(request, bAggregateSessions):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/test2018/')
    else:
        import csv
        from django.http import HttpResponse

        answer_list = Answer4.objects.all().order_by("id")
        
        result = {} # date --> { order --> { mydict } } 

        order_dict = {} #usernumber --> order-int

        order_int = 0

        mytz = GMT1()
        
        for answer4 in answer_list:
            usernumber = answer4.usernumber

            # Convert aware datetime into our own timezone
            mydate = answer4.date
            date = (u"%s" % mydate)[0:10]
            time = (u"%s" % mydate)[11:19]

            timelapse = answer4.timelapse
            rule_clicks = answer4.rule_clicks

            figure = answer4.figure
            quantor_1 = answer4.quantor_1
            quantor_2 = answer4.quantor_2
            quantor_3 = answer4.quantor_3

            term_S = term2string[answer4.term_S]
            term_M = term2string[answer4.term_M]
            term_P = term2string[answer4.term_P]

            correctness = answer4.correctness
            conclusion_truth_value = answer4.conclusion_truth_value
            student_answer = answer4.student_answer
            propkind = answer4.propkind
            

            if student_answer == "valid":
                if correctness:
                    syllogism_validity = "valid"
                else:
                    syllogism_validity = "invalid"
            else:
                if correctness:
                    syllogism_validity = "invalid"
                else:
                    syllogism_validity = "valid"

            if usernumber in order_dict:
                order = order_dict[usernumber]
            else:
                order = order_int
                order_int += 1
                order_dict[usernumber] = order

            result.setdefault(date, {})
            result[date].setdefault(order, [])

            result[date][order].append({
                "time" : time,
                "usernumber" : usernumber,
                "timelapse" : timelapse,
                "rule_clicks" : rule_clicks,
                
                "figure" : figure,
                "quantor_1" : quantor_1,
                "quantor_2" : quantor_2,
                "quantor_3" : quantor_3,

                "term_S" : term_S,
                "term_M" : term_M,
                "term_P" : term_P,
                
                "correctness" : correctness,
                "syllogism_validity" : syllogism_validity,
                "conclusion_truth_value" : conclusion_truth_value,
                "student_answer" : student_answer,
                "propkind" : propkind,
            })


    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse("", content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=logsyllog-data4.csv'

    writer = csv.writer(response)
    if not bAggregateSessions:
        first_row = ['date', 'time', 'usernumber', 'figure', 'quantor_1', 'quantor_2', 'quantor_3', 'term_S', 'term_M', 'term_P', 'conclusion_truth_value', 'syllogism_validity',  'answer_is_correct', 'answer', 'propkind', 'timelapse (s)', 'totaltime (s)', 'lastcorrectinarow', 'answercount', 'correctanswercount', 'rule_clicks']
    else:
        first_row = ['date', 'usernumber', 'totaltime (s)', 'lastcorrectinarow', 'answercount', 'correctanswercount', 'total_rule_clicks']
    writer.writerow(first_row)

    for date in sorted(result):
        for order in sorted(result[date]):
            usernumber = 0
            last_correct_in_a_row = 0
            totaltime = 0
            answercount = 0
            correctanswercount = 0
            total_rule_clicks = 0
            for mydict in result[date][order]:
                answercount += 1
                next_row = []
                next_row.append(date)
                next_row.append('%s' % mydict['time'])
                next_row.append('%d' % mydict['usernumber'])
                usernumber = mydict['usernumber']
                next_row.append('%d' % mydict['figure'])
                next_row.append('%s' % mydict['quantor_1'])
                next_row.append('%s' % mydict['quantor_2'])
                next_row.append('%s' % mydict['quantor_3'])
                next_row.append('%s' % mydict['term_S'])
                next_row.append('%s' % mydict['term_M'])
                next_row.append('%s' % mydict['term_P'])
                next_row.append('%s' % mydict['conclusion_truth_value'])
                next_row.append('%s' % mydict['syllogism_validity'])
                next_row.append('%s' % mydict['correctness'])
                next_row.append('%s' % mydict['student_answer'])
                next_row.append('%s' % mydict['propkind'])
                next_row.append('%.3f' % ((1.0 * mydict['timelapse']) / 1000.0))
                next_row.append('') # totaltime, only valid for the aggregate rows
                next_row.append('%d' % last_correct_in_a_row)
                next_row.append('%d' % answercount)
                next_row.append('%d' % correctanswercount)
                next_row.append('%d' % mydict['rule_clicks'])
                totaltime += mydict['timelapse']
                if not bAggregateSessions:
                    writer.writerow(next_row)
                del next_row

                if mydict["correctness"]:
                    last_correct_in_a_row += 1
                    correctanswercount += 1
                else:
                    last_correct_in_a_row = 0

                total_rule_clicks += mydict['rule_clicks']

            if not bAggregateSessions:
                next_row = [date, '', '%d' % usernumber, '', '', '', '', '', '', '', '', '', '', '', '', '', '%.3f' % ((1.0 * totaltime) / 1000.0), '%d' % last_correct_in_a_row, '%d' % answercount, '%d' % correctanswercount, '%d' % total_rule_clicks]
            else:
                next_row = [date, '%d' % usernumber, '%.3f' % ((1.0 * totaltime) / 1000.0), '%d' % last_correct_in_a_row, '%d' % answercount, '%d' % correctanswercount, '%d' % total_rule_clicks]
            writer.writerow(next_row)
            del next_row

    return response


def dump5(request):
    bAggregateSessions = False    
    return dump5_super(request, bAggregateSessions)
    
def dump5_aggregatesess(request):
    bAggregateSessions = True
    return dump5_super(request, bAggregateSessions)
    
def dump5_super(request, bAggregateSessions):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/test2018/')
    else:
        import csv
        from django.http import HttpResponse

        answer_list = Answer5.objects.all().order_by("id")
        
        result = {} # date --> { order --> { mydict } } 

        order_dict = {} #usernumber --> order-int

        order_int = 0

        mytz = GMT1()
        
        for answer5 in answer_list:
            usernumber = answer5.usernumber

            # Convert aware datetime into our own timezone
            mydate = answer5.date
            date = (u"%s" % mydate)[0:10]
            time = (u"%s" % mydate)[11:19]

            timelapse = answer5.timelapse

            figure = answer5.figure
            quantor_1 = answer5.quantor_1
            quantor_2 = answer5.quantor_2
            quantor_3 = answer5.quantor_3

            term_S = artificialterm2string[answer5.term_S]
            term_M = artificialterm2string[answer5.term_M]
            term_P = artificialterm2string[answer5.term_P]

            correctness = answer5.correctness
            conclusion_truth_value = answer5.conclusion_truth_value
            student_answer = answer5.student_answer
            propkind = answer5.propkind

            if student_answer == "valid":
                if correctness:
                    syllogism_validity = "valid"
                else:
                    syllogism_validity = "invalid"
            else:
                if correctness:
                    syllogism_validity = "invalid"
                else:
                    syllogism_validity = "valid"

            if usernumber in order_dict:
                order = order_dict[usernumber]
            else:
                order = order_int
                order_int += 1
                order_dict[usernumber] = order

            result.setdefault(date, {})
            result[date].setdefault(order, [])

            result[date][order].append({
                "time" : time,
                "usernumber" : usernumber,
                "timelapse" : timelapse,
                
                "figure" : figure,
                "quantor_1" : quantor_1,
                "quantor_2" : quantor_2,
                "quantor_3" : quantor_3,

                "term_S" : term_S,
                "term_M" : term_M,
                "term_P" : term_P,
                
                "correctness" : correctness,
                "syllogism_validity" : syllogism_validity,
                "conclusion_truth_value" : conclusion_truth_value,
                "student_answer" : student_answer,
                "propkind" : propkind,
            })


    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse("", content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=logsyllog-data5.csv'

    writer = csv.writer(response)
    if not bAggregateSessions:
        first_row = ['date', 'time', 'usernumber', 'figure', 'quantor_1', 'quantor_2', 'quantor_3', 'term_S', 'term_M', 'term_P', 'conclusion_truth_value', 'syllogism_validity',  'answer_is_correct', 'answer', 'propkind', 'timelapse (s)', 'totaltime (s)', 'lastcorrectinarow', 'answercount', 'correctanswercount']
    else:
        first_row = ['date', 'usernumber', 'totaltime (s)', 'lastcorrectinarow', 'answercount', 'correctanswercount']

    writer.writerow(first_row)

    for date in sorted(result):
        for order in sorted(result[date]):
            usernumber = 0
            last_correct_in_a_row = 0
            totaltime = 0
            answercount = 0
            correctanswercount = 0
            for mydict in result[date][order]:
                answercount += 1
                next_row = []
                next_row.append(date)
                next_row.append('%s' % mydict['time'])
                next_row.append('%d' % mydict['usernumber'])
                usernumber = mydict['usernumber']
                next_row.append('%d' % mydict['figure'])
                next_row.append('%s' % mydict['quantor_1'])
                next_row.append('%s' % mydict['quantor_2'])
                next_row.append('%s' % mydict['quantor_3'])
                next_row.append('%s' % mydict['term_S'])
                next_row.append('%s' % mydict['term_M'])
                next_row.append('%s' % mydict['term_P'])
                next_row.append('%s' % mydict['conclusion_truth_value'])
                next_row.append('%s' % mydict['syllogism_validity'])
                next_row.append('%s' % mydict['correctness'])
                next_row.append('%s' % mydict['student_answer'])
                next_row.append('%s' % mydict['propkind'])
                next_row.append('%.3f' % ((1.0 * mydict['timelapse']) / 1000.0))
                totaltime += mydict['timelapse']
                if not bAggregateSessions:
                    writer.writerow(next_row)
                del next_row

                if mydict["correctness"]:
                    last_correct_in_a_row += 1
                    correctanswercount += 1
                else:
                    last_correct_in_a_row = 0

            if not bAggregateSessions:
                next_row = [date, '', '%d' % usernumber, '', '', '', '', '', '', '', '', '', '', '', '', '', '%.3f' % ((1.0 * totaltime) / 1000.0), '%d' % last_correct_in_a_row, '%d' % answercount, '%d' % correctanswercount]
            else:
                next_row = [date, '%d' % usernumber, '%.3f' % ((1.0 * totaltime) / 1000.0), '%d' % last_correct_in_a_row, '%d' % answercount, '%d' % correctanswercount]

            writer.writerow(next_row)
            del next_row

    return response


