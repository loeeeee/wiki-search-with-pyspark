{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python 3.14
    (python314.withPackages (ps: with ps; [
      pip
      requests

      ### Jupyter
      jupyter
      ipykernel

      ### Visualization
      matplotlib
      seaborn

      ### Observerbility
      tqdm

      ### ML
      numpy
      pandas
      scikit-learn

      ### NLP
      spacy
      spacy-models.en_core_web_sm

      ### DL
      torch
      torchaudio
      torchvision

      ### Spark
      pyspark
      pyarrow
      grpcio
      grpcio-tools
      grpcio-status
    ]))

    # Java runtime for PySpark
    openjdk21
  ];

  shellHook = ''
    # Set JAVA_HOME for PySpark
    export JAVA_HOME=${pkgs.openjdk21}

    echo "Django development environment ready."
    echo "Python version: $(python --version)"
    echo "Django version: $(django-admin --version)"
  '';
}
