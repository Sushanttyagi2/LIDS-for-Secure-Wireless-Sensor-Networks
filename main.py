{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO267BVPm3kf6XpHbYTac41",
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
        "<a href=\"https://colab.research.google.com/github/Sushanttyagi2/LIDS-for-Secure-Wireless-Sensor-Networks/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from src.simulation import generate_data\n",
        "from src.model import train_model\n",
        "from src.detection import hybrid_detection\n",
        "\n",
        "import pandas as pd\n",
        "\n",
        "# Data generate\n",
        "normal = generate_data(500, False)\n",
        "attack = generate_data(200, True)\n",
        "df = pd.concat([normal, attack])\n",
        "\n",
        "# Train model\n",
        "model = train_model(df)\n",
        "\n",
        "# Test\n",
        "sample = [50, 0.5, 0.2]\n",
        "result = hybrid_detection(model, sample)\n",
        "\n",
        "print(\"Result:\", result)"
      ],
      "metadata": {
        "id": "LRfEc3AK1EF0"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}