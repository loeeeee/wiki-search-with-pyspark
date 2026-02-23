{ pkgs ? import <nixpkgs> {} }:

let
  django-bash-completion = pkgs.fetchurl {
    url = "https://raw.githubusercontent.com/django/django/refs/heads/main/extras/django_bash_completion";
    # A dummy hash is provided here. Nix will fail on the first run and provide the correct hash.
    sha256 = "sha256-fo4jzovjyffoKQDdz3k4qiAsT+QuhzdPCe0l+bogE88=";
  };
in
pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python 3.14
    (python314.withPackages (ps: with ps; [
      pip
      requests

      ### Observerbility
      tqdm

      ### Spark
      pyspark
      pyarrow
      grpcio
      grpcio-status
    ]))

    uv

    # Java runtime for PySpark
    openjdk21
  ];

  shellHook = ''
    # Set JAVA_HOME for PySpark
    export JAVA_HOME=${pkgs.openjdk21}

    # Django autocomplete
    source ${django-bash-completion}

    # Host Python version
    echo "Host Python version: $(python --version)"
    source .venv/bin/activate
    echo "entering UV environment"
    echo "venv Python version: $(python --version)"
  '';
}