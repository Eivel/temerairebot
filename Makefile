.PHONY: clean

setup:
	# Channel Travel config
	test -f config/files/channel_travel/channels.json || cp config/files/channel_travel/example/channels_example.json config/files/channel_travel/channels.json
	test -f config/files/channel_travel/whitelist.json || cp config/files/channel_travel/example/whitelist_example.json config/files/channel_travel/whitelist.json
	test -f config/files/channel_travel/message.txt || cp config/files/channel_travel/example/message_example.txt config/files/channel_travel/message.txt
