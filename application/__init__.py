def get_manifest_interface(filename: str, mode: str, encoding: str):
    return {
        'file': filename,
        'mode': mode,
        'encoding': encoding
    }