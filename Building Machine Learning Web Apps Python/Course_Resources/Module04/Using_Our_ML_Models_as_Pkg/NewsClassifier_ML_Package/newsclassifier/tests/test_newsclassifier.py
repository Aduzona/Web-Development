from newsclassifier import NewsClassifier 
from newsclassifier import __version__


def test_version():
	assert __version__ == '0.01'

def test_newsclassifier_for_text():
	n = NewsClassifier()
	mytext = """Nato leaders are meeting near London, as tensions between members threaten to overshadow a summit marking the military alliance's 70th birthday.The three-hour talks are expected to cover issues such as cyber-attacks and the strategic challenge posed by China.In opening remarks, UK Prime Minister Boris Johnson reminded members of the alliance's principle of "one for all, and all for one".Tuesday saw sharp exchanges between the US and French leaders over many topics.The highly choreographed anniversary gathering, intended to show unity, has been unable to hide deep differences between member states, BBC Defence Correspondent Jonathan Beale reports.Although the 29-member bloc's future is not in doubt, there are disagreements over Turkey's recent military action in northern Syria, the levels of military spending by members and recent comments by French President Emmanuel Macron that the alliance is "brain dead"."""
	n.text = mytext
	result = n.predict()
	assert result ==  'politics'
