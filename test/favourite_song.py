import main.ox
ox = main.ox.Ox()
ox.tell("What's your favourite song?")
logical_form = ox.conversation.context[0].content
func = logical_form[0]
args = logical_form[1]
print func(*args)
