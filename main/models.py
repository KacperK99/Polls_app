from django.db import models



class User(models.Model):
    ID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Poll(models.Model):
    ID = models.AutoField(primary_key=True)
    poll_name = models.CharField(max_length=50)
    poll_description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField()

class Question(models.Model):
    ID = models.AutoField(primary_key=True)
    question = models.CharField(max_length=120)
    is_single_choice = models.BooleanField(default=False)
    is_multi_choice = models.BooleanField(default=False)
    is_open = models.BooleanField(default=False)
    is_date_choice = models.BooleanField(default=False)

class Answer(models.Model):
    ID = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=120)
    is_marked = models.BooleanField(default=False)
    open_answer = models.TextField(blank=True, null=True)
    date_answer = models.BooleanField(default=False)

class GroupOfUsers(models.Model):
    ID = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=80)

class UserGroup(models.Model):
    ID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupOfUsers, on_delete=models.CASCADE)

class UserAnswer(models.Model):
    ID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

class UserPoll(models.Model):
    ID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)