music.set_built_in_speaker_enabled(False)
music.set_volume(93)
music.set_tempo(106)
music.play_tone(277, music.beat(BeatFraction.WHOLE))
music.play_tone(370, music.beat(BeatFraction.WHOLE))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(370, music.beat(BeatFraction.HALF))
music.play_tone(294, music.beat(BeatFraction.WHOLE))
music.play_tone(277, music.beat(BeatFraction.WHOLE))
basic.pause(1)
music.play_tone(247, music.beat(BeatFraction.HALF))
music.play_tone(277, music.beat(BeatFraction.HALF))
music.play_tone(220, music.beat(BeatFraction.WHOLE))
music.play_tone(247, music.beat(BeatFraction.HALF))
music.play_tone(262, music.beat(BeatFraction.HALF))
music.play_tone(277, music.beat(BeatFraction.WHOLE))
music.play_tone(220, music.beat(BeatFraction.WHOLE))
music.play_tone(208, music.beat(BeatFraction.HALF))
music.play_tone(220, music.beat(BeatFraction.HALF))
music.play_tone(247, music.beat(BeatFraction.HALF))
basic.pause(1)
music.play_tone(277, music.beat(BeatFraction.HALF))
music.play_tone(294, music.beat(BeatFraction.WHOLE))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(294, music.beat(BeatFraction.WHOLE))
music.play_tone(277, music.beat(BeatFraction.WHOLE))
music.play_tone(277, music.beat(BeatFraction.WHOLE))
music.play_tone(370, music.beat(BeatFraction.WHOLE))
basic.pause(1)
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(370, music.beat(BeatFraction.HALF))
music.play_tone(294, music.beat(BeatFraction.WHOLE))
music.play_tone(277, music.beat(BeatFraction.WHOLE))
music.play_tone(247, music.beat(BeatFraction.HALF))
music.play_tone(277, music.beat(BeatFraction.HALF))
music.play_tone(220, music.beat(BeatFraction.WHOLE))
music.play_tone(247, music.beat(BeatFraction.HALF))
music.play_tone(262, music.beat(BeatFraction.HALF))
music.play_tone(277, music.beat(BeatFraction.WHOLE))
basic.pause(1)
music.play_tone(220, music.beat(BeatFraction.WHOLE))
music.play_tone(208, music.beat(BeatFraction.HALF))
music.play_tone(220, music.beat(BeatFraction.HALF))
music.play_tone(247, music.beat(BeatFraction.HALF))
music.play_tone(277, music.beat(BeatFraction.HALF))
music.play_tone(294, music.beat(BeatFraction.WHOLE))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(294, music.beat(BeatFraction.WHOLE))
music.play_tone(277, music.beat(BeatFraction.WHOLE))

def on_forever():
    pass
basic.forever(on_forever)
