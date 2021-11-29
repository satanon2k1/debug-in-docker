def initialize_debugger():
    import multiprocessing

    if multiprocessing.current_process().pid > 1:
        import debugpy

        debugpy.listen(("0.0.0.0", 45678))
        print("Debugger is ready to be attached", flush=True)
        # debugpy.wait_for_client()
        # print("Visual Studio Code debugger is now attached", flush=True)