
def log(session,account):
	s=session.post("https://mbasic.facebook.com/login",
		data=
			{
				"email":account.split("|")[-0],
				"pass":account.split("|")[-1]
			}
	).url
	return "save-device" in s or "m_sess" in s
