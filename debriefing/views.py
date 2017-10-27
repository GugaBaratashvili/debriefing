from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail

# Create your views here.


def post_list(request):
	return render(request, 'blog/post/list.html')

def privacy(request):
	return render(request, 'blog/PrivacyAct.html')



def post_send(request):
	#retreive post by id
	send = False
	to = 'maia.bolkvadze.ln@mail.mil'
	if request.method == 'POST':
		#Form was submitted
		form = EmailPostForm(request.POST)
		if form.is_valid():
			#Form fields passed validation
			cd = form.cleaned_data
			#post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{} {} has sent you a Student Debriefing Questionnaire'.format(cd['First_Name'], cd['Last_Name'], )
			message = '{} {} {} \n\n {}\n\n{}\n\n1. Prior to departure for training in the U.S., did you receive a thorough briefing on travel arrangements? {}\n\n2. Did you have any problems in traveling to or from the U.S.? {}\n\n3. Was the training difficult? If so, what was (were) the reason(s)? {}\n\n{}\n\n4. Should the training you received be provided to other students? If not why not? {}\n\n{}\n\n5. Will you use the training received in your next military assignment? {}\n\n6. Did you receive adequate assistance from the school and base personnel? {}\n\n7. Were you treated with courtesy by the school and base personnel? {}\n\n8. Did you encounter any financial or pay problems? {}\n\n9. were you paid on time and have you received all the pay due to you? {}\n\n10. Were the allowances provided adequate for your housing and subsistence? {}\n\n11. Did the International Military Student Officer assist you enough in settling in and on other administrative and general matters? {}\n\n12. Were your sleeping quarters adequate? {}\n\n13. Did you receive additional help from instructors when you requested? {}\n\n14. Did you have enough study time and free time for sports and recreation? {}\n\n15. Did you experience any problems while in the U.S., other than those mentioned above? If so what were they and how were they solved.? {}\n\n{}\n\n16. Do you have any recommendations, suggestions, or general comments concerning your entire training cycle? {}\n\n{}'.format( cd['Rank'], cd['First_Name'], cd['Last_Name'], cd['Course'], cd['Course_Location'],cd['q1'], cd['q2'], cd['q3'], cd['q3comment'], cd['q4'], cd['q4comment'],cd['q5'],cd['q6'],cd['q7'],cd['q8'],cd['q9'],cd['q10'],cd['q11'],cd['q12'],cd['q13'],cd['q14'],cd['q15'], cd['q15comment'],cd['q16'], cd['q16comment'])
			send_mail(subject, message, 'debriefingsurvey@gmail.com', [to])
			send = True
	else:
		form = EmailPostForm()
	return render(request, 'blog/sent.html', {'form': form, 'send':send})


