from shema_viewer.ast_viewer import ast_pdf_viewer
from shema_viewer.cfg_viewer_pdf import cfg_pdf_viewer
from shema_viewer.pdg_viewer_pdf import pdg_pdf_viewer

if __name__ == '__main__':
    name_file_check = 'test_files/simple_lambda_file.py'
    with open(name_file_check, 'r') as file:
        code = file.read()
    ast_pdf_viewer(code)
    cfg_pdf_viewer(name_file_check)
    pdg_pdf_viewer(code)

