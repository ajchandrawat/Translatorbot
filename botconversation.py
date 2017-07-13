import json
from watson_developer_cloud import ConversationV1
from watson_developer_cloud import LanguageTranslatorV2
#########################
# Get input from user
#########################

def conversation_out():
	language_translator = LanguageTranslatorV2(
			username='dc47664f-73b6-4b61-96c9-73fcf1d07b99',
			password='i1AtnNfGTaYC')
	get_input=input()


	if get_input=="stop":
		exit()
	else:
		#########################000000000000000000000000000000000000000000000000000000000
		# Conversation API
		#########################

		conversation = ConversationV1(
			username='54b90e80-5b16-4912-a082-a81ce3a7f4f5',
			password='2YiLQK2ofLdV',
			version='2017-04-21')
		workspace_id = '55275262-9f80-47e5-9058-60824f100ca6'
		response = conversation.message(workspace_id=workspace_id, message_input={
			'text': get_input})
		outputvar=response['output']['text'][0]	
				# Output of conversation API
		if(get_input=="french"):
			print("Enter Text")
			outputvar=input()
			print(json.dumps(language_translator.translate(outputvar,source='en',target='fr'),ensure_ascii=False))
			conversation_out()
		elif(get_input=="spanish"):
			print("Enter Text")
			outputvar=input()
			print(json.dumps(language_translator.translate(outputvar,source='en',target='es'),ensure_ascii=False))
			conversation_out()
		elif(get_input=="arabic"):
			print("Enter Text")
			outputvar=input()
			print(json.dumps(language_translator.translate(outputvar,source='en',target='ar'),ensure_ascii=False))
			conversation_out()
		elif(get_input=="Brazilian"):
			print("Enter Text")
			outputvar=input()
			print(json.dumps(language_translator.translate(outputvar,source='en',target='br'),ensure_ascii=False))
			conversation_out()
		elif(get_input=="italian"):
			print("Enter Text")
			outputvar=input()
			print(json.dumps(language_translator.translate(outputvar,source='en',target='it'),ensure_ascii=False))
			conversation_out()
		else:
			print(outputvar)
			conversation_out()
conversation_out()