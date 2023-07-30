from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

# Replace YOUR_CHANNEL_SECRET and YOUR_CHANNEL_ACCESS_TOKEN with the actual values from LINE Developers Console
line_bot_api = LineBotApi('v87sy7Ijk4gRQ5C2QSBRVjVUMR4+8FGtv0OoWznwNNY3VlHoi45b8OVWrAXN2rfrpkxNAUHF5lsjvUZ65GkdQRTndnMaRz8WtjweWkXE7owhV56y/JC5oVcVnX9z13TkI88IIbzUA2zNg400V3mMOwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('cb38a398f37ac7e718f378d947ece1f8')
