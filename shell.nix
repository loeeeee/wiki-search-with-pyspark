{ pkgs ? import <nixpkgs> {} }:

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

    echo "Python version: $(python --version)"

    source .venv/bin/activate
    echo "entering UV environment"
  '';
}
