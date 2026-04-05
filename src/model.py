{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMvQoNgaHwBohtlP5OV+AXA",
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
        "<a href=\"https://colab.research.google.com/github/Sushanttyagi2/LIDS-for-Secure-Wireless-Sensor-Networks/blob/main/src/model.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "ttuhvOySxqku"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "def train_model(df):\n",
        "    X = df[[\"packet_rate\", \"drop_rate\", \"energy\"]]\n",
        "    y = df[\"label\"]\n",
        "\n",
        "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\n",
        "\n",
        "    model = DecisionTreeClassifier()\n",
        "    model.fit(X_train, y_train)\n",
        "\n",
        "    return model"
      ]
    }
  ]
}