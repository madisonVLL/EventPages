def most_common_key(list_of_dicts: list[dict[str, int]]) -> tuple[str, int]:
    ### add types above
   key_dict = {}
   for each in list_of_dicts:
      for key, _ in each.items():
         if key in key_dict.keys():
            key_dict[key] += 1
         else:
            key_dict[key] = 0
   
   return (max(key_dict.values()))