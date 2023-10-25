from staticfg import CFGBuilder


def cfg_pdf_viewer(file_name: str):
    cfg = CFGBuilder().build_from_file(file_name, file_name)

    cfg.build_visual('CFG - Control Flow Generator', 'pdf')


if __name__ == '__main__':
    cfg_pdf_viewer("../test_files/simple_lambda_file.py")
    cfg_pdf_viewer("../test_files/medium_lambda_file.py")