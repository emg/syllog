from django.db import models

# Create your models here.
class Answer(models.Model):
    usernumber = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    timelapse = models.IntegerField(default=0)
    syllnumber = models.IntegerField()
    figure = models.IntegerField()
    correctness = models.BooleanField(default=False)

    def __str__(self):
        return "%d: %s: %d/%d: correct: %s" % (self.usernumber, self.date, self.figure, self.syllnumber, self.correctness)


class Answer2(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    conclusion_truth_value = models.BooleanField(default=False)
    term_S = models.IntegerField(null=True)
    term_M = models.IntegerField(null=True)
    term_P = models.IntegerField(null=True)
    
    def __str__(self):
        return "%d: %s: %d/%d: correct: %s conclusion: %s S: %s M: %s P: %s" % (self.answer.usernumber, self.answer.date, self.answer.figure, self.answer.syllnumber, self.answer.correctness, self.conclusion_truth_value, self.term_S, self.term_M, self.term_P)

class Answer3(models.Model):
    """Answer3 is the model used for all versions of the syllogistic 
    valid/invalid experiments since around 2015."""
    
    QUANTOR_CHOICES = (
        ('au', 'All'),
        ('iu', 'Some'),
        ('eu', 'No'),
        ('ou', 'Some ... are not'),
        )

    VALIDITY_CHOICES = (
        ('valid', 'Valid'),
        ('invalid', 'Invalid'),
        )

    PROPKIND_CHOICES = (
        ('verbal', 'Verbal only'),
        ('graph', 'Verbal and CG'),
        )

    usernumber = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    timelapse = models.IntegerField(default=0)

    figure = models.IntegerField()
    quantor_1 = models.CharField(max_length=2, choices=QUANTOR_CHOICES)
    quantor_2 = models.CharField(max_length=2, choices=QUANTOR_CHOICES)
    quantor_3 = models.CharField(max_length=2, choices=QUANTOR_CHOICES)

    term_S = models.IntegerField(null=True)
    term_M = models.IntegerField(null=True)
    term_P = models.IntegerField(null=True)

    correctness = models.BooleanField(default=False)
    conclusion_truth_value = models.BooleanField(default=False)
    student_answer = models.CharField(max_length=7, choices=VALIDITY_CHOICES)
    propkind = models.CharField(max_length=10, choices=PROPKIND_CHOICES)
    
    def __str__(self):
        return "%d: %s: (%d,%s,%s,%s): correct: %s conclusion: %s answer: %s propkind: %s S: %s M: %s P: %s" % (self.usernumber, self.date, self.figure, self.quantor_1, self.quantor_2, self.quantor_3, self.correctness, self.conclusion_truth_value, self.student_answer, self.propkind, self.term_S, self.term_M, self.term_P)

class Answer5(models.Model):
    QUANTOR_CHOICES = (
        ('au', 'All'),
        ('iu', 'Some'),
        ('eu', 'No'),
        ('ou', 'Some ... are not'),
        )

    VALIDITY_CHOICES = (
        ('valid', 'Valid'),
        ('invalid', 'Invalid'),
        )

    PROPKIND_CHOICES = (
        ('verbal', 'Verbal only'),
        ('graph', 'Verbal and CG'),
        )

    usernumber = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    timelapse = models.IntegerField(default=0)

    figure = models.IntegerField()
    quantor_1 = models.CharField(max_length=2, choices=QUANTOR_CHOICES)
    quantor_2 = models.CharField(max_length=2, choices=QUANTOR_CHOICES)
    quantor_3 = models.CharField(max_length=2, choices=QUANTOR_CHOICES)

    term_S = models.IntegerField(null=True)
    term_M = models.IntegerField(null=True)
    term_P = models.IntegerField(null=True)

    correctness = models.BooleanField(default=False)
    conclusion_truth_value = models.BooleanField(default=False)
    student_answer = models.CharField(max_length=7, choices=VALIDITY_CHOICES)
    propkind = models.CharField(max_length=10, choices=PROPKIND_CHOICES)
    
    def __str__(self):
        return "%d: %s: (%d,%s,%s,%s): correct: %s conclusion: %s answer: %s propkind: %s S: %s M: %s P: %s" % (self.usernumber, self.date, self.figure, self.quantor_1, self.quantor_2, self.quantor_3, self.correctness, self.conclusion_truth_value, self.student_answer, self.propkind, self.term_S, self.term_M, self.term_P)

class Answer4(models.Model):
    """Answer4 is for logging the experiments that determine whether
    students are able to prove that a syllogism is valid or invalid,
    using the rules Trans, Subst, Contra, Ex and (optionally) Mut.

    This is logged with the /logsyllog/log4/ URL.

    The following front-ends (at a minimum) were meant for this model:

    - test6
    - test8
    - proof

    """

    QUANTOR_CHOICES = (
        ('au', 'All'),
        ('iu', 'Some'),
        ('eu', 'No'),
        ('ou', 'Some ... are not'),
        )

    VALIDITY_CHOICES = (
        ('valid', 'Valid'),
        ('invalid', 'Invalid'),
        )

    PROPKIND_CHOICES = (
        ('verbal', 'Verbal only'),
        ('graph', 'Verbal and CG'),
        )

    usernumber = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    timelapse = models.IntegerField(default=0)
    rule_clicks = models.IntegerField(default=0)

    figure = models.IntegerField()
    quantor_1 = models.CharField(max_length=2, choices=QUANTOR_CHOICES)
    quantor_2 = models.CharField(max_length=2, choices=QUANTOR_CHOICES)
    quantor_3 = models.CharField(max_length=2, choices=QUANTOR_CHOICES)

    term_S = models.IntegerField(null=True)
    term_M = models.IntegerField(null=True)
    term_P = models.IntegerField(null=True)

    correctness = models.BooleanField(default=False)
    conclusion_truth_value = models.BooleanField(default=False)
    student_answer = models.CharField(max_length=7, choices=VALIDITY_CHOICES)
    propkind = models.CharField(max_length=10, choices=PROPKIND_CHOICES)
    
    
    def __str__(self):
        return "%d: %s: (%d,%s,%s,%s): rule_clicks: %d correct: %s conclusion: %s answer: %s propkind: %s S: %s M: %s P: %s" % (self.usernumber, self.date, self.figure, self.quantor_1, self.quantor_2, self.quantor_3, self.rule_clicks, self.correctness, self.conclusion_truth_value, self.student_answer, self.propkind, self.term_S, self.term_M, self.term_P)
    
