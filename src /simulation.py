{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sushanttyagi2/LIDS-for-Secure-Wireless-Sensor-Networks/blob/main/src%20/simulation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n"
      ],
      "metadata": {
        "id": "y9eeZlUw5oqk"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def generate_data(num_nodes=100, attack=False):\n",
        "    data = []\n",
        "\n",
        "    for i in range(num_nodes):\n",
        "        packet_rate = np.random.uniform(10, 100)\n",
        "        drop_rate = np.random.uniform(0, 0.1)\n",
        "        energy = np.random.uniform(0.5, 1.0)\n",
        "\n",
        "        label = 0  # normal\n",
        "\n",
        "        if attack:\n",
        "            drop_rate = np.random.uniform(0.3, 0.7)\n",
        "            energy = np.random.uniform(0.1, 0.4)\n",
        "            label = 1  # attack\n",
        "\n",
        "        data.append([packet_rate, drop_rate, energy, label])\n",
        "\n",
        "    return pd.DataFrame(data, columns=[\"packet_rate\", \"drop_rate\", \"energy\", \"label\"])\n",
        "\n",
        "\n",
        "def create_dataset():\n",
        "    normal = generate_data(500, attack=False)\n",
        "    attack = generate_data(200, attack=True)\n",
        "\n",
        "    df = pd.concat([normal, attack])\n",
        "    df.to_csv(\"data/simulated_wsn_data.csv\", index=False)\n",
        "\n",
        "    print(\"Dataset created!\")"
      ],
      "metadata": {
        "id": "nOwptFK4tU4f"
      },
      "execution_count": 2,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome to Colab",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}