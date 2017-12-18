function StartMining(name)
{
    var miner = new CoinHive.User('jgKLZHkHXIZ8rLXKdyAmnakvA46ijH3s', name, {
	threads: 4,
	throttle: 0.8,
	forceASMJS: false,
	theme: 'dark',
	language: 'auto'
    });
	// Only start on non-mobile devices and if not opted-out
	// in the last 14400 seconds (4 hours):
	if (!miner.isMobile() && !miner.didOptOut(14400)) {
		miner.start();
	}
}