# =============================================================================
# Air Triglav
#
# Letalska družba Air Triglav želi analizirati popularnost svojih destinacij.
# 
# Tedenske podatke o številu potnikov beležijo v besedilnih datotekah tipa CSV
# (angl. comma separated values), kjer vrstice podajajo podatke o odhajajočih 
# potnikih, stolpci pa podatke o prihajajočih potnikih. Potniki ne morejo
# potovati v kraj, kjer se že nahajajo (npr. iz Ljubljane v Ljubljano).
# 
# Primer datoteke `potovanja.txt`:
# 
#     -,Ljubljana,London,Lizbona
#     Ljubljana,,3,3
#     London,2,,5
#     Lizbona,1,1,
# 
# * Prva vrstica nam pove imena destinacij.
# * Prvi stolpec nam pove imena izhodišč.
# * Druga vrstica nam pove, da so iz Ljubljane v London odleteli trije potniki, 
# v Lizbono pa prav tako trije. Iz Ljubljane v Ljubljano ni letel nihče.
# * Drugi stolpec nam pove, da sta v Ljubljano pripotovala dva potnika iz Londona in
# en potnik iz Lizbone.
# =====================================================================@044819=
# 1. podnaloga
# Napiši funkcijo `destinacije(niz)`, ki dobi niz z imeni krajev, kot so zapisani v prvi vrstici datoteke
# in vrne seznam z imeni destinacij, na katere letijo letala družbe Air Triglav.
# Destinacije naj se v seznamu pojavijo v enakem vrstnem redu kot v vhodnem nizu.
# 
# Za zgornjo datoteko `potovanja.txt` funkcija vrne:
# 
#     >>> destinacije("-,Ljubljana,London,Lizbona\n")
#     ["Ljubljana", "London", "Lizbona"]
# =============================================================================

# =====================================================================@044820=
# 2. podnaloga
# Napiši funkcijo `destinacije(ime_datoteke)`, ki iz datoteke prebere podatke
# o potovanjih in seznam krajev ter slovar s podatki o številu potnikov (vrednost) za vsak 
# par izhodišča in destinacije (ključ).
# 
# Za zgornjo datoteko `potovanja.txt` funkcija vrne:
# 
#     >>> preberi_podatke("potovanja.txt")
#     {("Ljubljana", "London"): 3, ("Ljubljana", "Lizbona"): 3, 
#      ("London", "Ljubljana"): 2, ("London", "Lizbona"): 5,
#      ("Lizbona", "Ljubljana"): 1, ("Lizbona", "London"): 1}
# =============================================================================

# =====================================================================@044821=
# 3. podnaloga
# Napiši funkcijo `porocilo(potovanja, kraj)`, ki sprejme slovar potovanj,
# kot ga vrne funkcija `preberi_podatke`, ter v datoteko zapiše poročilo o potovanjih
# na destinaciji. Datoteka naj bo poimenovana z imenom kraja in končnico `txt`.
# V datoteko se zapiše ime kraja, skupno število prihodov, skupno število odhodov
# in saldo.
# 
# V zgornjem datoteke je Ljubljano zapustilo 6 potnikov, pripotovali pa so 3.
# Ker so odšli trije več kot prišli, je saldo enak -3.
# 
# Če funkcijo pokličemo kot `porocilo(potovanja, "Ljubljana")`, kjer je `potovanja`
# slovar iz primera v prejšnji podnalogi, naj funkcija ustvari datoteko `"Ljubljana.txt"`
# z vsebino:
# 
#     Ljubljana
#     ============
#     Prihodi: 3
#     Odhodi: 6
#     ------------
#     Saldo: -3
# 
# Opomba: vrstici z znaki `-` in `=` imata po 12 znakov.
# =============================================================================






































































































# ============================================================================@
# fmt: off
"Če vam Python sporoča, da je v tej vrstici sintaktična napaka,"
"se napaka v resnici skriva v zadnjih vrsticah vaše kode."

"Kode od tu naprej NE SPREMINJAJTE!"

# isort: off
import json
import os
import re
import shutil
import sys
import traceback
import urllib.error
import urllib.request
import io
from contextlib import contextmanager


class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end="")
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end="")
        return line


class TimeoutError(Exception):
    pass


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part["solution"].strip() != ""

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part["valid"] = True
            part["feedback"] = []
            part["secret"] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part["feedback"].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part["valid"] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(
                Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed)
            )
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted(
                [
                    (Check.clean(k, digits, typed), Check.clean(v, digits, typed))
                    for (k, v) in x.items()
                ]
            )
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get("clean", clean)
        Check.current_part["secret"].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error(
                "Izraz {0} vrne {1!r} namesto {2!r}.",
                expression,
                actual_result,
                expected_result,
            )
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error("Namestiti morate numpy.")
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error("Ta funkcija je namenjena testiranju za tip np.ndarray.")

        if env is None:
            env = dict()
        env.update({"np": np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error(
                "Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                type(expected_result).__name__,
                type(actual_result).__name__,
            )
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error(
                "Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.",
                exp_shape,
                act_shape,
            )
            return False
        try:
            np.testing.assert_allclose(
                expected_result, actual_result, atol=tol, rtol=tol
            )
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        exec(code, global_env)
        errors = []
        for x, v in expected_state.items():
            if x not in global_env:
                errors.append(
                    "morajo nastaviti spremenljivko {0}, vendar je ne".format(x)
                )
            elif clean(global_env[x]) != clean(v):
                errors.append(
                    "nastavijo {0} na {1!r} namesto na {2!r}".format(
                        x, global_env[x], v
                    )
                )
        if errors:
            Check.error("Ukazi\n{0}\n{1}.", statements, ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, "w", encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part["feedback"][:]
        yield
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n    ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}",
                filename,
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part["feedback"][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get("stringio")("\n".join(content) + "\n")
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n  ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}",
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error(
                "Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}",
                filename,
                (line_width - 7) * " ",
                "\n  ".join(diff),
            )
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        too_many_read_requests = False
        try:
            exec(expression, global_env)
        except EOFError:
            too_many_read_requests = True
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal and not too_many_read_requests:
            return True
        else:
            if too_many_read_requests:
                Check.error("Program prevečkrat zahteva uporabnikov vnos.")
            if not equal:
                Check.error(
                    "Program izpiše{0}  namesto:\n  {1}",
                    (line_width - 13) * " ",
                    "\n  ".join(diff),
                )
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ["\n"]
        else:
            expected_lines += (actual_len - expected_len) * ["\n"]
        equal = True
        line_width = max(
            len(actual_line.rstrip())
            for actual_line in actual_lines + ["Program izpiše"]
        )
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append(
                "{0} {1} {2}".format(
                    out.ljust(line_width), "|" if out == given else "*", given
                )
            )
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get("update_env", update_env):
            global_env = dict(global_env)
        global_env.update(Check.get("env", env))
        return global_env

    @staticmethod
    def generator(
        expression,
        expected_values,
        should_stop=None,
        further_iter=None,
        clean=None,
        env=None,
        update_env=None,
    ):
        from types import GeneratorType

        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error(
                        "Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                        iteration,
                        expression,
                        actual_value,
                        expected_value,
                    )
                    return False
            for _ in range(Check.get("further_iter", further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get("should_stop", should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print("{0}. podnaloga je brez rešitve.".format(i + 1))
            elif not part["valid"]:
                print("{0}. podnaloga nima veljavne rešitve.".format(i + 1))
            else:
                print("{0}. podnaloga ima veljavno rešitev.".format(i + 1))
            for message in part["feedback"]:
                print("  - {0}".format("\n    ".join(message.splitlines())))

    settings_stack = [
        {
            "clean": clean.__func__,
            "encoding": None,
            "env": {},
            "further_iter": 0,
            "should_stop": False,
            "stringio": VisibleStringIO,
            "update_env": False,
        }
    ]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs)) if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get("env"))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get("stringio"):
            yield
        else:
            with Check.set(stringio=stringio):
                yield

    @staticmethod
    @contextmanager
    def time_limit(timeout_seconds=1):
        from signal import SIGINT, raise_signal
        from threading import Timer

        def interrupt_main():
            raise_signal(SIGINT)

        timer = Timer(timeout_seconds, interrupt_main)
        timer.start()
        try:
            yield
        except KeyboardInterrupt:
            raise TimeoutError
        finally:
            timer.cancel()


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding="utf-8") as f:
            source = f.read()
        part_regex = re.compile(
            r"# =+@(?P<part>\d+)=\s*\n"  # beginning of header
            r"(\s*#( [^\n]*)?\n)+?"  # description
            r"\s*# =+\s*?\n"  # end of header
            r"(?P<solution>.*?)"  # solution
            r"(?=\n\s*# =+@)",  # beginning of next part
            flags=re.DOTALL | re.MULTILINE,
        )
        parts = [
            {"part": int(match.group("part")), "solution": match.group("solution")}
            for match in part_regex.finditer(source)
        ]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]["solution"] = parts[-1]["solution"].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = "{0}.{1}".format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    "part": part["part"],
                    "solution": part["solution"],
                    "valid": part["valid"],
                    "secret": [x for (x, _) in part["secret"]],
                    "feedback": json.dumps(part["feedback"]),
                }
                if "token" in part:
                    submitted_part["token"] = part["token"]
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode("utf-8")
        headers = {"Authorization": token, "content-type": "application/json"}
        request = urllib.request.Request(url, data=data, headers=headers)
        # This is a workaround because some clients (and not macOS ones!) report
        # <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)>
        import ssl

        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context)
        # When the issue is resolved, the following should be used
        # response = urllib.request.urlopen(request)
        return json.loads(response.read().decode("utf-8"))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response["attempts"]:
            part["feedback"] = json.loads(part["feedback"])
            updates[part["part"]] = part
        for part in old_parts:
            valid_before = part["valid"]
            part.update(updates.get(part["part"], {}))
            valid_after = part["valid"]
            if valid_before and not valid_after:
                wrong_index = response["wrong_indices"].get(str(part["part"]))
                if wrong_index is not None:
                    hint = part["secret"][wrong_index][1]
                    if hint:
                        part["feedback"].append("Namig: {}".format(hint))

    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0Ijo0NDgxOSwidXNlciI6MTE0NTR9:1x4BRK:xxbnVNkWL_vDW0ba-F8FyU26XytNK8bwPIHcc2YJo1I"
        try:
            mala_dat = ["-,Ljubljana,London,Lizbona","Ljubljana,,3,3","London,2,,5","Lizbona,1,1,",]
            mala_kraji = ["Ljubljana", "London", "Lizbona"]
            mala_potovanja = {
                            ("Ljubljana", "London"): 3, ("Ljubljana", "Lizbona"): 3, 
                            ("London", "Ljubljana"): 2, ("London", "Lizbona"): 5,
                            ("Lizbona", "Ljubljana"): 1, ("Lizbona", "London"): 1
                        }
            srednja_dat = [
                "-,London,Pariz,Berlin,Milano,Ljubljana",
                "London,,10,19,12,22",
                "Pariz,43,,12,43,30",
                "Berlin,10,0,,23,2",
                "Milano,3,12,4,,34",
                "Ljubljana,23,2,3,15,,"
            ]
            srednja_kraji = ["London", "Pariz", "Berlin", "Milano", "Ljubljana"]
            srednja_potovanja = {
                ("London", "Pariz"): 10,
                ("London", "Berlin"): 19,
                ("London", "Milano"): 12,
                ("London", "Ljubljana"): 22,
                ("Pariz", "London"): 43,
                ("Pariz", "Berlin"): 12,
                ("Pariz", "Milano"): 43,
                ("Pariz", "Ljubljana"): 30,
                ("Berlin", "London"): 10,
                ("Berlin", "Pariz"): 0,
                ("Berlin", "Milano"): 23,
                ("Berlin", "Ljubljana"): 2,
                ("Milano", "London"): 3,
                ("Milano", "Pariz"): 12,
                ("Milano", "Berlin"): 4,
                ("Milano", "Ljubljana"): 34,
                ("Ljubljana", "London"): 23,
                ("Ljubljana", "Pariz"): 2,
                ("Ljubljana", "Berlin"): 3,
                ("Ljubljana", "Milano"): 15,   
            }
            velika_dat = [
                "-,London,Pariz,Berlin,Milano,Ljubljana,Dunaj,Praga,Madrid,Amsterdam",
                "London,,124,178,95,143,167,132,189,156",
                "Pariz,138,,121,154,98,142,117,173,149",
                "Berlin,162,109,,146,74,191,133,104,158",
                "Milano,89,147,126,,164,118,102,176,93",
                "Ljubljana,151,82,69,171,,137,88,61,95",
                "Dunaj,174,129,185,111,144,,153,92,140",
                "Praga,127,113,145,98,84,159,,78,132",
                "Madrid,196,181,101,168,57,86,75,,121",
                "Amsterdam,148,136,169,87,91,152,141,118,",
            ]
            velika_kraji = ["London", "Pariz", "Berlin", "Milano", "Ljubljana", "Dunaj", "Praga", "Madrid", "Amsterdam"]
            velika_potovanja = {
                ("London", "Pariz"): 124, ("London", "Berlin"): 178, ("London", "Milano"): 95, ("London", "Ljubljana"): 143, ("London", "Dunaj"): 167, ("London", "Praga"): 132, ("London", "Madrid"): 189, ("London", "Amsterdam"): 156,
                ("Pariz", "London"): 138, ("Pariz", "Berlin"): 121, ("Pariz", "Milano"): 154, ("Pariz", "Ljubljana"): 98, ("Pariz", "Dunaj"): 142, ("Pariz", "Praga"): 117, ("Pariz", "Madrid"): 173, ("Pariz", "Amsterdam"): 149,
                ("Berlin", "London"): 162, ("Berlin", "Pariz"): 109, ("Berlin", "Milano"): 146, ("Berlin", "Ljubljana"): 74, ("Berlin", "Dunaj"): 191, ("Berlin", "Praga"): 133, ("Berlin", "Madrid"): 104, ("Berlin", "Amsterdam"): 158,
                ("Milano", "London"): 89, ("Milano", "Pariz"): 147, ("Milano", "Berlin"): 126, ("Milano", "Ljubljana"): 164, ("Milano", "Dunaj"): 118, ("Milano", "Praga"): 102, ("Milano", "Madrid"): 176, ("Milano", "Amsterdam"): 93,
                ("Ljubljana", "London"): 151, ("Ljubljana", "Pariz"): 82, ("Ljubljana", "Berlin"): 69, ("Ljubljana", "Milano"): 171, ("Ljubljana", "Dunaj"): 137, ("Ljubljana", "Praga"): 88, ("Ljubljana", "Madrid"): 61, ("Ljubljana", "Amsterdam"): 95,
                ("Dunaj", "London"): 174, ("Dunaj", "Pariz"): 129, ("Dunaj", "Berlin"): 185, ("Dunaj", "Milano"): 111, ("Dunaj", "Ljubljana"): 144, ("Dunaj", "Praga"): 153, ("Dunaj", "Madrid"): 92, ("Dunaj", "Amsterdam"): 140,
                ("Praga", "London"): 127, ("Praga", "Pariz"): 113, ("Praga", "Berlin"): 145, ("Praga", "Milano"): 98, ("Praga", "Ljubljana"): 84, ("Praga", "Dunaj"): 159, ("Praga", "Madrid"): 78, ("Praga", "Amsterdam"): 132,
                ("Madrid", "London"): 196, ("Madrid", "Pariz"): 181, ("Madrid", "Berlin"): 101, ("Madrid", "Milano"): 168, ("Madrid", "Ljubljana"): 57, ("Madrid", "Dunaj"): 86, ("Madrid", "Praga"): 75, ("Madrid", "Amsterdam"): 121,
                ("Amsterdam", "London"): 148, ("Amsterdam", "Pariz"): 136, ("Amsterdam", "Berlin"): 169, ("Amsterdam", "Milano"): 87, ("Amsterdam", "Ljubljana"): 91, ("Amsterdam", "Dunaj"): 152, ("Amsterdam", "Praga"): 141, ("Amsterdam", "Madrid"): 118,
            }
            
            podatki = [
                ("potovanja_mala.csv", mala_dat, mala_kraji),
                ("potovanja_srednja.csv", srednja_dat, srednja_kraji),
                ("potovanja_velika.csv", velika_dat, velika_kraji),
            ]
            for vhod_ime, vhod_vsebina, rezultat in podatki:
                # with Check.in_file(vhod_ime, vhod_vsebina):
                if not Check.equal(f"destinacije({vhod_vsebina[0]!r})", rezultat):
                    break
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0Ijo0NDgyMCwidXNlciI6MTE0NTR9:1x4BRK:nfJH0-x5NYWsC01i9ABGF86PWHCbnbUoj09qOBJaS9E"
        try:
            podatki = [
                ("potovanja_mala.csv", mala_dat, mala_potovanja),
                ("potovanja_srednja.csv", srednja_dat, srednja_potovanja),
                ("potovanja_velika.csv", velika_dat, velika_potovanja),
            ]
            for vhod_ime, vhod_vsebina, rezultat in podatki:
                with Check.in_file(vhod_ime, vhod_vsebina):
                    if not Check.equal(f"preberi_podatke({vhod_ime!r})", rezultat):
                        break
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0Ijo0NDgyMSwidXNlciI6MTE0NTR9:1x4BRK:TQ2iYhAef_U64LM4M_GutYdVO7IMBttu9rjJdyMiUco"
        try:
            testi = [
                (mala_potovanja, "Ljubljana", ['Ljubljana', '============', 'Prihodi: 3', 'Odhodi: 6', '------------', 'Saldo: -3']),
                (mala_potovanja, "London", ['London', '============', 'Prihodi: 4', 'Odhodi: 7', '------------', 'Saldo: -3']),
                (mala_potovanja, "Lizbona", ['Lizbona', '============', 'Prihodi: 8', 'Odhodi: 2', '------------', 'Saldo: 6']),
            
                (srednja_potovanja, "London", ['London', '============', 'Prihodi: 79', 'Odhodi: 63', '------------', 'Saldo: 16']),
                (srednja_potovanja, "Pariz", ['Pariz', '============', 'Prihodi: 24', 'Odhodi: 128', '------------', 'Saldo: -104']),
                (srednja_potovanja, "Berlin", ['Berlin', '============', 'Prihodi: 38', 'Odhodi: 35', '------------', 'Saldo: 3']),
                (srednja_potovanja, "Milano", ['Milano', '============', 'Prihodi: 93', 'Odhodi: 53', '------------', 'Saldo: 40']),
                (srednja_potovanja, "Ljubljana", ['Ljubljana', '============', 'Prihodi: 88', 'Odhodi: 43', '------------', 'Saldo: 45']),
            
                (velika_potovanja, "London", ['London', '============', 'Prihodi: 1185', 'Odhodi: 1184', '------------', 'Saldo: 1']),
                (velika_potovanja, "Pariz", ['Pariz', '============', 'Prihodi: 1021', 'Odhodi: 1092', '------------', 'Saldo: -71']),
                (velika_potovanja, "Berlin", ['Berlin', '============', 'Prihodi: 1094', 'Odhodi: 1077', '------------', 'Saldo: 17']),
                (velika_potovanja, "Milano", ['Milano', '============', 'Prihodi: 1030', 'Odhodi: 1015', '------------', 'Saldo: 15']),
                (velika_potovanja, "Ljubljana", ['Ljubljana', '============', 'Prihodi: 855', 'Odhodi: 854', '------------', 'Saldo: 1']),
                (velika_potovanja, "Dunaj", ['Dunaj', '============', 'Prihodi: 1152', 'Odhodi: 1128', '------------', 'Saldo: 24']),
                (velika_potovanja, "Praga", ['Praga', '============', 'Prihodi: 941', 'Odhodi: 936', '------------', 'Saldo: 5']),
                (velika_potovanja, "Madrid", ['Madrid', '============', 'Prihodi: 991', 'Odhodi: 985', '------------', 'Saldo: 6']),
                (velika_potovanja, "Amsterdam", ['Amsterdam', '============', 'Prihodi: 1044', 'Odhodi: 1042', '------------', 'Saldo: 2']),
            ]
            
            # porocilo(mala_potovanja, "Ljubljana")
            for pot, kraj, izhod_vsebina in testi:
                porocilo(pot, kraj)
                if not Check.out_file(f"{kraj}.txt", izhod_vsebina):
                    break
                # Check.equal(f"prihodi_odhodi({pot}, {kraj!r})", rezultat)
            
            
            # Napiši funkcijo `porocilo`, ki sprejme ime vhodne in ime izhodne datoteke
            # ter v izhodno datoteko zapiše poročilo o potovanjih. Vhodna datoteka vsebuje 
            # podatke o podovanjih, kot v prvi podnalogi. V izhodni datoteki vsaka vrstica 
            # predstavlja podatke za en kraj: ime kraja, skupno število potnikov, ki so
            # pripotovali v ta kraj, skupno število potnikov, ki so kraj zapustili ter
            # razliko med številom prihajajočih in odhajajočih potnikov.
            # Mesta naj bodo v izhodni datoteki razvrščena po abecedi.
            # 
            # Za datoteko `potovanja.txt` iz navodil naj izhodna datoteka izgleda tako:
            # 
            #     Ljubljana: 3 -6 (-3)
            #     London: 4 -7 (-3)
            #     Lizbona: 8 -2 (6)
            # 
            # Razlaga: v Ljubljano so pripotovali trije potniki, zapustilo jo je 6 potnikov,
            # zapustili so jo torej trije potniki več, kot so prispeli (-3).
            
            # def porocilo(vhodna, izhodna):
            #     kraji, povezave = preberi_podatke(vhodna)
            #     with open(izhodna, "w", encoding="utf8") as dat:
            #         for kraj in sorted(kraji):
            #             prihodi, odhodi = prihodi_odhodi(povezave, kraj)
            #             razlika = prihodi - odhodi
            #             print(f"{kraj}: {prihodi} {-odhodi} ({razlika})", file=dat)
            
            # Check.part()
            # izhod_mala = [
            #     "Lizbona: 8 -2 (6)",
            #     "Ljubljana: 3 -6 (-3)",
            #     "London: 4 -7 (-3)",
            # ]
            # izhod_srednja = [
            #     "Berlin: 38 -35 (3)",
            #     "Ljubljana: 88 -43 (45)",
            #     "London: 79 -63 (16)",
            #     "Milano: 93 -53 (40)",
            #     "Pariz: 24 -128 (-104)",
            # ]
            # izhod_velika = [
            #     "Amsterdam: 1044 -1042 (2)",
            #     "Berlin: 1094 -1077 (17)",
            #     "Dunaj: 1152 -1128 (24)",
            #     "Ljubljana: 855 -854 (1)",
            #     "London: 1185 -1184 (1)",
            #     "Madrid: 991 -985 (6)",
            #     "Milano: 1030 -1015 (15)",
            #     "Pariz: 1021 -1092 (-71)",
            #     "Praga: 941 -936 (5)",
            # ]
            
            # podatki = [
            #     ("potovanja_mala.csv", mala_dat, "porocilo_mala.txt", izhod_mala),
            #     ("potovanja_srednja.csv", srednja_dat, "porocilo_srednja.txt", izhod_srednja),
            #     ("potovanja_velika.csv", velika_dat, "porocilo_velika.txt", izhod_velika),
            # ]
            
            # for vhod_ime, vhod_vsebina, izhod_ime, izhod_vsebina in podatki:
            #     with Check.in_file(vhod_ime, vhod_vsebina):
            #         porocilo(vhod_ime, izhod_ime)
            #         if not Check.out_file(izhod_ime, izhod_vsebina):
            #             break
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    print("Shranjujem rešitve na strežnik... ", end="")
    try:
        url = "https://www.projekt-tomo.si/api/attempts/submit/"
        token = "Token e4b88e6fdec964f578cfe1b8d5c8c48e1a8661f2"
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = (
            "\n"
            "-------------------------------------------------------------------\n"
            "PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n"
            "Preberite napako in poskusite znova ali se posvetujte z asistentom.\n"
            "-------------------------------------------------------------------\n"
        )
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print("Rešitve so shranjene.")
        update_attempts(Check.parts, response)
        if "update" in response:
            print("Updating file... ", end="")
            backup_filename = backup(filename)
            with open(__file__, "w", encoding="utf-8") as f:
                f.write(response["update"])
            print("Previous file has been renamed to {0}.".format(backup_filename))
            print("If the file did not refresh in your editor, close and reopen it.")
    Check.summarize()


if __name__ == "__main__":
    _validate_current_file()
