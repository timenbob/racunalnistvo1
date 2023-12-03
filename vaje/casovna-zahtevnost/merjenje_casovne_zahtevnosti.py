# =============================================================================
# Merjenje časovne zahtevnosti
#
# Če za algoritem nimamo na voljo izvorne kode, časovne zahtevnosti ne moremo
# oceniti drugače, kot da jo poskušamo izmeriti. Če odkomentirate vrstico
# 
#     # import zlib, base64; exec(zlib.decompress(base64.b64decode('eJwll7eu...
# 
# v priloženi kodi, naložite definicijo 14 funkcij, katerih časovno zahtevnost
# boste merili pri tej nalogi. Funkcije kot vhod sprejmejo celo število `n`,
# glede na katerega časovno zahtevnost ocenjujemo.
# =====================================================================@038425=
# 1. podnaloga
# Funkcije `f1a`, `f1b`, `f1c`, `f1d` in `f1e` imajo časovne zahtevnosti oblike
# $O(n^k)$ za nek neznani $k$. V spremenljivko `potence1` shranite nabor potenc
# časovnih zahtevnosti posameznih funkcij. Na primer, če bi imele funkcije
# časovne zahtevnosti $O(n^3)$, $O(n)$, $O(n^4)$, $O(n)$ in $O(n^2)$, bi v
# spremenljivko `potence1` shranili nabor `(3, 1, 4, 1, 2)`.
# =============================================================================
# import zlib, base64; exec(zlib.decompress(base64.b64decode('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')))
# =====================================================================@038426=
# 2. podnaloga
# V spremenljivko `potence2` shranite nabor potenc časovnih zahtevnosti funkcij
# `f2a`, `f2b`, `f2c`, `f2d` in `f2e`.
# =============================================================================

# =====================================================================@038427=
# 3. podnaloga
# V spremenljivko `potence3` shranite nabor potenc časovnih zahtevnosti funkcij
# `f3a`, `f3b`, `f3c` in `f3d`.
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
        ] = "eyJwYXJ0IjozODQyNSwidXNlciI6NTM2MX0:1r8e7n:nK72Tga9PqNoEsCSmWNPGnqkNSjPakzhR-LMLG7udQE"
        try:
            if not isinstance(potence1, tuple):
                Check.error('Spremenljivka potence1 ni nabor.')
            elif len(potence1) != 5:
                Check.error('Spremenljivka potence1 mora vsebovati 5 elementov.')
            elif not all(isinstance(potenca, int) for potenca in potence1):
                Check.error('Spremenljivka potence1 mora vsebovati samo cela števila.')
            elif not all(potenca >= 0 for potenca in potence1):
                Check.error('Spremenljivka potence1 mora vsebovati samo nenegativna števila.')
            Check.secret(potence1)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODQyNiwidXNlciI6NTM2MX0:1r8e7n:8I3N66MOgWbGghIyDzxblEPi1aIK3T2o-chXD2voBeU"
        try:
            if not isinstance(potence2, tuple):
                Check.error('Spremenljivka potence2 ni nabor.')
            elif len(potence2) != 5:
                Check.error('Spremenljivka potence2 mora vsebovati 5 elementov.')
            elif not all(isinstance(potenca, int) for potenca in potence2):
                Check.error('Spremenljivka potence2 mora vsebovati samo cela števila.')
            elif not all(potenca >= 0 for potenca in potence2):
                Check.error('Spremenljivka potence2 mora vsebovati samo nenegativna števila.')
            Check.secret(potence2)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0IjozODQyNywidXNlciI6NTM2MX0:1r8e7n:aSOsFAR9GOxfDXJ6xGtERfYWBi_Y4strTYmJZL4mkmI"
        try:
            if not isinstance(potence3, tuple):
                Check.error('Spremenljivka potence3 ni nabor.')
            elif len(potence3) != 4:
                Check.error('Spremenljivka potence3 mora vsebovati 4 elemente.')
            elif not all(isinstance(potenca, int) for potenca in potence3):
                Check.error('Spremenljivka potence3 mora vsebovati samo cela števila.')
            elif not all(potenca >= 0 for potenca in potence3):
                Check.error('Spremenljivka potence3 mora vsebovati samo nenegativna števila.')
            Check.secret(potence3)
        except:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    print("Shranjujem rešitve na strežnik... ", end="")
    try:
        url = "https://www.projekt-tomo.si/api/attempts/submit/"
        token = "Token 6ed02d48c90356a789434661991772050d001e9a"
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
