import quickcodec

quickcodec.logging.set_level(quickcodec.logging.VERBOSE)

input_ = quickcodec.open("resources/webvtt.mkv")
output = quickcodec.open("remuxed.vtt", "w")

in_stream = input_.streams.subtitles[0]
out_stream = output.add_stream_from_template(in_stream)

for packet in input_.demux(in_stream):
    if packet.dts is None:
        continue
    packet.stream = out_stream
    output.mux(packet)

input_.close()
output.close()

print("Remuxing done")

with quickcodec.open("remuxed.vtt") as f:
    for subset in f.decode(subtitles=0):
        for sub in subset:
            print(sub.ass)
