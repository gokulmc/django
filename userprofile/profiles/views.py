# work_form# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied



@login_required
def edit_user(request):
    user = request.user
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('website', 'bio', 'phone', 'city', 'country', 'organization'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile/')

        return render(request, "template.html", {
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied


@login_required
def profile(request):
    user = request.user
    user_form = UserProfileForm(instance=user)
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('website', 'bio', 'phone', 'city', 'country', 'organization'))
    formset = ProfileInlineFormset(instance=user)
    return render(request, "template.html", {
        "noodle_form": user_form,
        "formset": formset,
    })


# @login_required
# @transaction.atomic
# def add_work(request):
#     if request.method == 'POST':
#         user_form = UserProfileForm(request.POST, instance=request.user)
#         work_form = WorkForm(request.POST, instance=request.user.work) #create a new work row with the user field filled
#         if user_form.is_valid() and work_form.is_valid():
#             user_form.save()
#             work_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         work_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         # 'user_form': user_form,
#         'work_form': work_form
#     })
