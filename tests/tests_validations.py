from src.utils.validations import validateExit, validateStringInput

def tests_string_input_passeds():
    assert validateStringInput("joaaao") == True
    assert validateStringInput("    joaoo") == True
    assert validateStringInput("joaoo       ") == True
    assert validateStringInput("    joaao     ") == True

def tests_string_input_fails():
    assert validateStringInput("") == False
    assert validateStringInput("jo4o") == False
    assert validateStringInput("!talo") == False
    assert validateStringInput("P3dr0 aa") == False
    assert validateStringInput("pedro aa") == False
    assert validateStringInput("     pedro aa         ") == False

def tests_exit_passeds():
    assert validateExit("SIM") == True
    assert validateExit("Sim") == True
    assert validateExit("sim") == True
    assert validateExit("     sim") == True
    assert validateExit("sim       ")
    assert validateExit("     sim         ") == True
    assert validateExit("       SIM      ") == True
    assert validateExit("NÃO") == True
    assert validateExit("NAO") == True
    assert validateExit("não") == True
    assert validateExit("nao") == True
    assert validateExit("       NÃO") == True
    assert validateExit("     NAO") == True
    assert validateExit("     NAO     ") == True
    assert validateExit("      Não     ") == True
    assert validateExit("      nao     ") == True
    assert validateExit("S") == True
    assert validateExit("s") == True
    assert validateExit("    s") == True
    assert validateExit("s     ") == True
    assert validateExit("    s    ") == True
    assert validateExit("N") == True
    assert validateExit("n") == True
    assert validateExit("     n") == True
    assert validateExit("n        ") == True
    assert validateExit("     n    ") == True

def tests_exit_fails():
    assert validateExit("") == False
    assert validateExit("n4o") == False
    assert validateExit("n40") == False
    assert validateExit("   aaa ") == False
    assert validateExit("!! ") == False
    assert validateExit("akoadanao ") == False    
    assert validateExit("33nao ") == False
