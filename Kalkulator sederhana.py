{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM2BgARRIWchui2yZnvWr7x",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/adjamahfud-arch/Proyek-coding-/blob/main/Kalkulator%20sederhana.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3lon0c7R87A8",
        "outputId": "05a88798-f97c-4d0c-fb1a-b39fea20eb5f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "==kalkulator sederhana==\n",
            "masukan nama mu:Mahfud \n",
            " : 60\n",
            " : *\n",
            " : 5\n",
            "------------------------------\n",
            "300.0\n",
            "------------------------------\n",
            "mau main lagi? ya/tidak:T\n",
            "==daftar nama orang yang memainkan kalkulator==\n",
            "Mahfud \n",
            "terimakasih sudah mencoba program saya\n"
          ]
        }
      ],
      "source": [
        "#sitem oprasi utama\n",
        "\n",
        "def kalkulator(angka, angka2, oprasi):\n",
        "    if oprasi == \"+\":\n",
        "       return angka + angka2\n",
        "    elif oprasi == \"-\":\n",
        "       return angka - angka2\n",
        "    elif oprasi == \"/\":\n",
        "       return float(angka / angka2)\n",
        "\n",
        "    elif oprasi == \"*\":\n",
        "       return angka * angka2\n",
        "#variable\n",
        "nama = []\n",
        "#sistem daftar nama\n",
        "def nama_orang():\n",
        "    for orang in nama:\n",
        "        print(orang)\n",
        "#input\n",
        "print(\"==kalkulator sederhana==\")\n",
        "pilih = \"ya\"\n",
        "\n",
        "while pilih == \"ya\":\n",
        "      orang =input(\"masukan nama mu:\")\n",
        "      nama.append(orang)\n",
        "      angka =float(input(\" : \"))\n",
        "      oprasi =input(\" : \")\n",
        "      angka2 =int(input(\" : \"))\n",
        "      hasil =kalkulator(angka, angka2, oprasi)\n",
        "      print(\"-\" * 30)\n",
        "      print(hasil)\n",
        "      print(\"-\" * 30)\n",
        "      pilih =input(\"mau main lagi? ya/tidak:\")\n",
        "#hasil\n",
        "print(\"==daftar nama orang yang memainkan kalkulator==\")\n",
        "\n",
        "nama_orang()\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "print(\"terimakasih sudah mencoba program saya\")"
      ]
    }
  ]
}