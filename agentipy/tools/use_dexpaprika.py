import aiohttp
from typing import Dict, List, Optional, Any, Union

from agentipy.agent import SolanaAgentKit


class DexPaprikaManager:
    BASE_URL = "https://api.dexpaprika.com"

    @staticmethod
    async def get_networks(agent: SolanaAgentKit) -> Dict[str, Any]:
        """
        Retrieve a list of all supported blockchain networks and their metadata.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.

        Returns:
            Dict[str, Any]: List of supported networks with metadata like display names.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/networks"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to fetch networks: {response.status}")
                    data = await response.json()
                    return data
        except Exception as e:
            raise Exception(f"Error fetching networks from DexPaprika: {e}")

    @staticmethod
    async def get_network_dexes(
        agent: SolanaAgentKit, 
        network: str, 
        page: int = 0, 
        limit: int = 10,
        sort: str = "desc"
    ) -> Dict[str, Any]:
        """
        Get a list of available decentralized exchanges on a specific network.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.
            network (str): Network ID (e.g., ethereum, solana).
            page (int, optional): Page number for pagination. Defaults to 0.
            limit (int, optional): Number of items per page. Defaults to 10.
            sort (str, optional): Sort order. Defaults to "desc".

        Returns:
            Dict[str, Any]: List of DEXes on the specified network.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/networks/{network}/dexes?page={page}&limit={limit}&sort={sort}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to fetch network DEXes: {response.status}")
                    data = await response.json()
                    return data
        except Exception as e:
            raise Exception(f"Error fetching network DEXes from DexPaprika: {e}")

    @staticmethod
    async def get_top_pools(
        agent: SolanaAgentKit, 
        order_by: str = "volume_usd", 
        sort: str = "desc", 
        page: int = 0, 
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        Get a paginated list of top liquidity pools from all networks.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.
            order_by (str, optional): Field to order by. Defaults to "volume_usd".
                Options: "volume_usd", "price_usd", "transactions", "last_price_change_usd_24h", "created_at".
            sort (str, optional): Sort order. Defaults to "desc".
                Options: "asc", "desc".
            page (int, optional): Page number for pagination. Defaults to 0.
            limit (int, optional): Number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: List of top liquidity pools with price data and tokens.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/pools?order_by={order_by}&sort={sort}&page={page}&limit={limit}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to fetch top pools: {response.status}")
                    data = await response.json()
                    return data
        except Exception as e:
            raise Exception(f"Error fetching top pools from DexPaprika: {e}")

    @staticmethod
    async def get_network_pools(
        agent: SolanaAgentKit, 
        network: str, 
        order_by: str = "volume_usd", 
        sort: str = "desc", 
        page: int = 0, 
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        Get a list of top liquidity pools on a specific network.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.
            network (str): Network ID (e.g., ethereum, solana).
            order_by (str, optional): Field to order by. Defaults to "volume_usd".
                Options: "volume_usd", "price_usd", "transactions", "last_price_change_usd_24h", "created_at".
            sort (str, optional): Sort order. Defaults to "desc".
                Options: "asc", "desc".
            page (int, optional): Page number for pagination. Defaults to 0.
            limit (int, optional): Number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: List of top liquidity pools for the specified network.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/networks/{network}/pools?order_by={order_by}&sort={sort}&page={page}&limit={limit}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to fetch network pools: {response.status}")
                    data = await response.json()
                    return data
        except Exception as e:
            raise Exception(f"Error fetching network pools from DexPaprika: {e}")

    @staticmethod
    async def get_dex_pools(
        agent: SolanaAgentKit, 
        network: str, 
        dex: str, 
        order_by: str = "volume_usd", 
        sort: str = "desc", 
        page: int = 0, 
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        Get top pools on a specific DEX within a network.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.
            network (str): Network ID (e.g., ethereum, solana).
            dex (str): DEX identifier.
            order_by (str, optional): Field to order by. Defaults to "volume_usd".
                Options: "volume_usd", "price_usd", "transactions", "last_price_change_usd_24h", "created_at".
            sort (str, optional): Sort order. Defaults to "desc".
                Options: "asc", "desc".
            page (int, optional): Page number for pagination. Defaults to 0.
            limit (int, optional): Number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: List of top pools for the specified DEX with price data.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/networks/{network}/dexes/{dex}/pools?order_by={order_by}&sort={sort}&page={page}&limit={limit}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to fetch DEX pools: {response.status}")
                    data = await response.json()
                    return data
        except Exception as e:
            raise Exception(f"Error fetching DEX pools from DexPaprika: {e}")

    @staticmethod
    async def get_pool_details(
        agent: SolanaAgentKit, 
        network: str, 
        pool_address: str, 
        inversed: bool = False
    ) -> Dict[str, Any]:
        """
        Get detailed information about a specific pool on a network.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.
            network (str): Network ID (e.g., ethereum, solana).
            pool_address (str): Pool address or identifier.
            inversed (bool, optional): Whether to invert the price ratio. Defaults to False.

        Returns:
            Dict[str, Any]: Detailed information about the specified pool including token pairs,
                current price data, and volume metrics across multiple time frames.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/networks/{network}/pools/{pool_address}?inversed={str(inversed).lower()}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to fetch pool details: {response.status}")
                    data = await response.json()
                    return data
        except Exception as e:
            raise Exception(f"Error fetching pool details from DexPaprika: {e}")

    @staticmethod
    async def get_token_details(
        agent: SolanaAgentKit, 
        network: str, 
        token_address: str
    ) -> Dict[str, Any]:
        """
        Get detailed information about a specific token on a network.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.
            network (str): Network ID (e.g., ethereum, solana).
            token_address (str): Token address or identifier.

        Returns:
            Dict[str, Any]: Detailed information about the specified token including 
                latest price, metadata, status, and recent summary metrics.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/networks/{network}/tokens/{token_address}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to fetch token details: {response.status}")
                    data = await response.json()
                    return data
        except Exception as e:
            raise Exception(f"Error fetching token details from DexPaprika: {e}")

    @staticmethod
    async def get_token_pools(
        agent: SolanaAgentKit, 
        network: str, 
        token_address: str, 
        address: Optional[str] = None, 
        order_by: str = "volume_usd", 
        sort: str = "desc", 
        page: int = 0, 
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        Get a list of top liquidity pools for a specific token on a network.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.
            network (str): Network ID (e.g., ethereum, solana).
            token_address (str): Token address or identifier.
            address (str, optional): Filter pools that contain this additional token address. Defaults to None.
            order_by (str, optional): Field to order by. Defaults to "volume_usd".
                Options: "volume_usd", "price_usd", "transactions", "last_price_change_usd_24h", "created_at".
            sort (str, optional): Sort order. Defaults to "desc".
                Options: "asc", "desc".
            page (int, optional): Page number for pagination. Defaults to 0.
            limit (int, optional): Number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: List of top liquidity pools for the specified token.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/networks/{network}/tokens/{token_address}/pools?order_by={order_by}&sort={sort}&page={page}&limit={limit}"
            
            if address:
                url += f"&address={address}"
                
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to fetch token pools: {response.status}")
                    data = await response.json()
                    return data
        except Exception as e:
            raise Exception(f"Error fetching token pools from DexPaprika: {e}")

    @staticmethod
    async def get_pool_ohlcv(
        agent: SolanaAgentKit, 
        network: str, 
        pool_address: str, 
        start: str, 
        end: Optional[str] = None, 
        interval: str = "24h", 
        inversed: bool = False, 
        limit: int = 1
    ) -> Dict[str, Any]:
        """
        Get OHLCV (Open-High-Low-Close-Volume) data for a specific pool.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.
            network (str): Network ID (e.g., ethereum, solana).
            pool_address (str): Pool address or identifier.
            start (str): Start time for historical data (ISO-8601, yyyy-mm-dd, or Unix timestamp).
            end (str, optional): End time for historical data (max 1 year from start). Defaults to None.
            interval (str, optional): Interval granularity for OHLCV data. Defaults to "24h".
                Options: "1m", "5m", "10m", "15m", "30m", "1h", "6h", "12h", "24h".
            inversed (bool, optional): Whether to invert the price ratio in OHLCV calculations. Defaults to False.
            limit (int, optional): Number of data points to retrieve (max 366). Defaults to 1.

        Returns:
            Dict[str, Any]: OHLCV data for the specified pool.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/networks/{network}/pools/{pool_address}/ohlcv?start={start}&interval={interval}&inversed={str(inversed).lower()}&limit={limit}"
            
            if end:
                url += f"&end={end}"
                
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to fetch pool OHLCV data: {response.status}")
                    data = await response.json()
                    
                    # Add ohlcv key if it doesn't exist (for compatibility with our tests)
                    if "data" in data and "ohlcv" not in data:
                        data["ohlcv"] = data["data"]
                    
                    return data
        except Exception as e:
            raise Exception(f"Error fetching pool OHLCV data from DexPaprika: {e}")

    @staticmethod
    async def get_pool_transactions(
        agent: SolanaAgentKit, 
        network: str, 
        pool_address: str, 
        page: int = 0, 
        limit: int = 10, 
        cursor: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get transactions of a pool on a network.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.
            network (str): Network ID (e.g., ethereum, solana).
            pool_address (str): Pool address or identifier.
            page (int, optional): Page number for pagination. Defaults to 0.
            limit (int, optional): Number of items per page. Defaults to 10.
            cursor (str, optional): Transaction ID used for cursor-based pagination. Defaults to None.

        Returns:
            Dict[str, Any]: List of transactions for the specified pool.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/networks/{network}/pools/{pool_address}/transactions?page={page}&limit={limit}"
            
            if cursor:
                url += f"&cursor={cursor}"
                
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to fetch pool transactions: {response.status}")
                    data = await response.json()
                    return data
        except Exception as e:
            raise Exception(f"Error fetching pool transactions from DexPaprika: {e}")

    @staticmethod
    async def search(
        agent: SolanaAgentKit, 
        query: str
    ) -> Dict[str, Any]:
        """
        Search for tokens, pools, and DEXes by name or identifier.

        Args:
            agent (SolanaAgentKit): The Solana agent instance.
            query (str): Search term (e.g., "uniswap", "bitcoin", or a token address).

        Returns:
            Dict[str, Any]: Search results containing matching tokens, pools, and DEXes.
        """
        try:
            url = f"{DexPaprikaManager.BASE_URL}/search?query={query}"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Failed to search: {response.status}")
                    data = await response.json()
                    return data
        except Exception as e:
            raise Exception(f"Error searching DexPaprika: {e}") 