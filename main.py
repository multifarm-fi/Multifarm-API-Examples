import requests


def run_query(query, variables):
    request = requests.post("https://commercial.multifarm.fi/graphql", json={"query": query, "variables": variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


query = """
{
  asset{
    assetId
    aprDaily
    aprHistory {
      date
      value
    }
    aprWeekly
    aprYearly
    apyYearly
    asset
    assetAddress
    assetLockup
    assetPopupMessage
    assetPrice
    auditInfo
    blockchain
    category
    collateralLockPeriod
    dateAdded
    dateEnding
    dateStarted
    dateUpdated
    daysRemaining
    depositFee
    exchangeName
    exchangePicture
    exchangeUrl
    exchangeVersion
    farm
    farmId
    farmImage
    harvestLockup
    harvestLockupInfo
    impermanentLoss
    impermanentLoss30d
    info
    investmentLink
    manuallyCalculatedAPR
    maxPoolCap
    multiplier
    nativeToken
    nativeTokenAddress
    nativeTokenInvestLink
    nativeTokenMarketCap
    nativeTokenPrice
    otherFees
    otherPoolEconomicsInfo
    poolAlreadyFilled
    rewardTokenA
    rewardTokenAAddress
    rewardTokenAPrice
    rewardTokenAWeeklyAmount
    rewardTokenAWeeklyDollarAmount
    rewardTokenB
    rewardTokenBAddress
    rewardTokenBPrice
    rewardTokenBWeeklyAmount
    rewardTokenBWeeklyDollarAmount
    rewardTokenPriceHistory {
      date
      value
    }
    scam
    scamInfo
    stakingAddress
    stakingLink
    tokenA
    tokenAAddress
    tokenAPicture
    tokenAPrice
    tokenB
    tokenBAddress
    tokenBPicture
    tokenBPrice
    tokenC
    tokenCAddress
    tokenCPicture
    tokenCPrice
    tokenD
    tokenDAddress
    tokenDPicture
    tokenDPrice
    transferTax
    transferTaxInfo
    tvlChange24h
    tvlChange24hValue
    tvlExchange
    tvlStaked
    tvlStakedHistory {
      date
      value
    }
    underlyingFarm
    url
    vaultAddress
    weight
    withdrawalFee
    yearlyTokenRewardPool
    yieldType
  }
}
"""

variables = {
    "api_key": "YOUR_API_KEY",
    "find": {"tvlStaked": {"$gt": 1000}},
}


result = run_query(query, variables)
print(result)
