from asyncio.windows_events import NULL
from ctypes.wintypes import HINSTANCE
from site import USER_BASE
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from core.models import Record

from mcq.forms import questionForm
from mcq.models import questionModel

from .models import cohortInfos, cohort

from .forms import createCohortForm,addMemberForm
from django.contrib.auth.models import User
from .models import QuesModel, ExamInfo
from .forms import addQuestionform, addExamForm
from core.views import record



# Create your views here.

def addCohort(request):
    if request.method == 'POST':
        form = createCohortForm(request.POST)
        if form.is_valid():
            u = request.user
            name = form.cleaned_data['name']
            chrt = cohort(CohortName = name , Admin = u.email)
            chrt.save()
            chrtInfo = cohortInfos(cohort = chrt, Member = u, MemberStatus = 'admin')
            chrtInfo.save()
            return HttpResponseRedirect('/dashboard')
    else:
        form = createCohortForm() 
    return render(request, 'cohort/createcohort.html', {'f': form})

def cohortIndex(request,cID):
    chrt = cohort.objects.get(CohortID = cID)
    cohortInformation = cohortInfos.objects.get(cohort = chrt , Member = request.user)
    exams = ExamInfo.objects.filter(cohort = chrt)

    if request.user.email == cohortInformation.cohort.Admin:
        return render(request, 'cohort/cohortIndexAdmin.html',{'Info':cohortInformation, 'exams': exams})
    else:
        return render(request, 'cohort/cohortIndexExaminee.html',{'Info':cohortInformation, 'exams': exams})

def addMember(request,cID):
    chrt = cohort.objects.get(CohortID = cID)
    cohortInformation = cohortInfos.objects.get(cohort = chrt, Member = request.user)
    if request.method == 'POST':
        form = addMemberForm(request.POST)
        messages.success(request, 'Examinee added successfully')
        if form.is_valid():
            email = form.cleaned_data['memberEmail']
            member = User.objects.get(email__exact = email)
            cohortadd = cohortInfos(cohort = chrt, Member = member, MemberStatus = "examinee")
            cohortadd.save()
            form = addMemberForm()
    else:
        form = addMemberForm()

    memberlist = cohortInfos.objects.filter(cohort = chrt)    

    return render(request, 'cohort/addMember.html',{'f':form, 'memberlist':memberlist})

def createExam(request, cID):
    chrt = cohort.objects.get(CohortID = cID)
    if request.method == 'POST':
        form = addExamForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['examName']
            type = form.cleaned_data['examType']
            exam = ExamInfo(examName = name, cohort = chrt, examType = type)
            exam.save()
            url = "/cohort/cohortIndex/"+cID
            return HttpResponseRedirect(url)
    else:
        form = addExamForm()

    return render(request, 'exam/addExam.html',{'f':form,})

def examIndex(request, cID, eID):
    chrt = cohort.objects.get(CohortID = cID)
    exxam = ExamInfo.objects.get(examID = eID)
    member = cohortInfos.objects.get(cohort = chrt, Member = request.user)

    questions = QuesModel.objects.filter(examID = exxam.examID)

    if request.user.email == chrt.Admin:
        return render(request, 'exam/examIndexAdmin.html',{'questions':questions, 'Info':chrt, 'exam':exxam})
    if request.user == member.Member and member.MemberStatus == 'examinee':
        if request.method == 'POST':
            print(request.POST)
            score=0
            wrong=0
            correct=0
            total=0
            for q in questions:
                total+=1
                if q.ans ==  request.POST[q.question]:
                    score+=1
                    correct+=1
                else:
                    wrong+=1
            context = {
                'score':score,
                'correct':correct,
                'wrong':wrong,
                'total':total,
            }
            return render(request, 'exam/result.html', context)
        else:
            return render(request, 'exam/examIndexExaminee.html',{'questions':questions, 'Info':chrt, 'exam':exxam})

def createQuestion(request, cID, eID):
    chrt = cohort.objects.get(CohortID = cID)
    exxam = ExamInfo.objects.get(examID = eID)
    c = chrt.CohortID
    e = exxam.examID
    if exxam.examType == 'Quiz':
        if request.method == 'POST':
            form = addQuestionform(request.POST)
            if form.is_valid():
                ques = form.cleaned_data['question']
                opt1 = form.cleaned_data['op1']
                opt2 = form.cleaned_data['op2']
                opt3 = form.cleaned_data['op3']
                opt4 = form.cleaned_data['op4']
                ansr = form.cleaned_data['ans']
                questions = QuesModel(question = ques, op1 = opt1, op2 = opt2, op3 = opt3, op4 = opt4, ans = ansr, examID = eID)
                questions.save()
                url = "/cohort/cohortIndex/"+cID+"/examIndex/"+eID+"/createquestion/"
                return HttpResponseRedirect(url)
        else:
            form = addQuestionform()
    elif exxam.examType == 'Micro-Viva':
        return render(request, 'exam/addViva.html',{'eID':e})
    return render(request, 'exam/addquestion.html', {'form':form})





  
