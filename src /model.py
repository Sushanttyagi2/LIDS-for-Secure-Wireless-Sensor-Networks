{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMf7AWUJ2hpOe2oO6mq1UDa",
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
        "<a href=\"https://colab.research.google.com/github/Sushanttyagi2/LIDS-for-Secure-Wireless-Sensor-Networks/blob/main/src%20/model.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "ttuhvOySxqku"
      },
      "outputs": [],
      "source": [
        "def rule_based_detection(packet_rate, drop_rate, energy):\n",
        "    if drop_rate > 0.3 or energy < 0.3:\n",
        "        return 1\n",
        "    return 0\n",
        "\n",
        "\n",
        "def hybrid_detection(model, sample):\n",
        "    ml_pred = model.predict([sample])[0]\n",
        "    rule_pred = rule_based_detection(*sample)\n",
        "\n",
        "    if ml_pred == 1 or rule_pred == 1:\n",
        "        return \"ATTACK\"\n",
        "    return \"NORMAL\""
      ]
    }
  ]
}