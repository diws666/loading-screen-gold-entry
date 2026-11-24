import os

TIP = "Tip: if your agent says the fix is simple, save your work, close the tab, and go for a walk. It is not simple."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TIP.encode("utf-8"))


if __name__ == "__main__":
    main()
