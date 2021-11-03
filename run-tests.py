import compiler
import interp_Pvar
from utils import run_tests

compiler = compiler.Compiler()

run_tests("var", compiler, "var", None, interp_Pvar.InterpPvar().interp_P, None, None)
