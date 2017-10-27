from django import forms

class EmailPostForm(forms.Form):
	CHOICES=[('Yes','Yes'),
         ('No','No')]
	#name = forms.CharField(max_length=25)
	#email = forms.EmailField()
	#to = forms.EmailField()
	#comments = forms.CharField(required=True, widget=forms.Textarea)
	First_Name = forms.CharField(max_length=25, required=True)
	Last_Name = forms.CharField(max_length=40, required=True)
	Rank = forms.CharField(max_length=30, required=True)
	#ito = forms.CharField(max_length=20, required=True)
	Course = forms.CharField(max_length=150, required=True)
	Course_Location = forms.CharField(max_length=100, required=True)
	q1 = forms.ChoiceField(label='1. Prior to departure for training in the U.S., did you receive a thorough briefing on travel arrangements?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q2 = forms.ChoiceField(label='2. Did you have any problems in traveling to or from the U.S.?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q3 = forms.ChoiceField(label='3. Was the training difficult? If so, what was (were) the reason(s)?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q3comment = forms.CharField(label='', widget=forms.Textarea, required=False)
	q4 = forms.ChoiceField(label='4. Should the training you received be provided to other students? If not why not?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q4comment = forms.CharField(label='', widget=forms.Textarea, required=False)
	q5 = forms.ChoiceField(label='5. Will you use the training received in your next military assignment?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q6 = forms.ChoiceField(label='6. Did you receive adequate assistance from the school and base personnel?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q7 = forms.ChoiceField(label='7. Were you treated with courtesy by the school and base personnel?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q8 = forms.ChoiceField(label='8. Did you encounter any financial or pay problems?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q9 = forms.ChoiceField(label='9. were you paid on time and have you received all the pay due to you?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q10 = forms.ChoiceField(label='10. Were the allowances provided adequate for your housing and subsistence?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q11 = forms.ChoiceField(label='11. Did the International Military Student Officer assist you enough in settling in and on other administrative and general matters?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q12 = forms.ChoiceField(label='12. Were your sleeping quarters adequate?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q13 = forms.ChoiceField(label='13. Did you receive additional help from instructors when you requested?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q14 = forms.ChoiceField(label='14. Did you have enough study time and free time for sports and recreation?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q15 = forms.ChoiceField(label='15. Did you experience any problems while in the U.S., other than those mentioned above? If so what were they and how were they solved?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q15comment = forms.CharField(label='', widget=forms.Textarea, required=False)
	q16 = forms.ChoiceField(label='16. Do you have any recommendations, suggestions, or general comments concerning your entire training cycle?', required=True, choices=CHOICES, widget=forms.RadioSelect())
	q16comment = forms.CharField(label='', widget=forms.Textarea, required=False)


