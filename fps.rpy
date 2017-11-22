init python:
    import time

    class __FixedFPSMeter(object):
        last_time = time.time()
        last_frame = config.frames

        def __call__(self, st, at):
            import time

            frames = config.frames - self.last_frame
            d_time = time.time() - self.last_time
            if d_time == 0:
                text = "FPS: Infinite"
            else:
                text = "FPS: %.2f" % ((frames or 1) / d_time)

            __FixedFPSMeter.last_frame = config.frames
            __FixedFPSMeter.last_time = time.time()

            return Text(text, xalign=1.0), .5


label fix_fps:
    python:
        config.overlay_functions.append(lambda: ui.add(DynamicDisplayable(__FixedFPSMeter())))
        store.suppress_overlay = False