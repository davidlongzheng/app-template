import { Movie } from "./types";
import camelcaseKeys from 'camelcase-keys';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function fetchApi<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    credentials: 'include',  // Important for cookies if using authentication
  });

  if (!response.ok) {
    throw new Error(`API call failed: ${response.statusText}`);
  }

  const data = await response.json();
  // Transform snake_case to camelCase recursively
  return camelcaseKeys(data, { deep: true });
}

// Example usage for specific API calls
export const api = {
  // Example method to fetch movies
  async getNewMovies(year: number, rating: number) {
    return fetchApi<Movie[]>(`/movies/new?year=${year}&rating=${rating}`);
  },
  
  // Add other API methods as needed
};
