
import LinkWizard
import LinkWizardRu
import data

try:
    while True:
        if data.launge=="ru":
            LinkWizardRu.launcher()
        if data.launge=="eng":
            LinkWizard.launcher()
except:
    pass
